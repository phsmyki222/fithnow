
import os
import sys
import json
import base64
import getpass
import time
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

VAULT = Path("PHRINUSOMYIS_SECURE_REGISTRY.vault")
LOCKOUT = Path("PHRINUSOMYIS_SECURITY.lock")
MAX_ATTEMPTS = 5
LOCKOUT_SECONDS = 300


class PhrinusomyisSecureRegistry:

    def derive_key(self, password, salt):
        kdf = Scrypt(
            salt=salt,
            length=32,
            n=2**15,
            r=8,
            p=1
        )
        return base64.urlsafe_b64encode(
            kdf.derive(password.encode("utf-8"))
        )

    def initialize(self):
        if VAULT.exists():
            raise RuntimeError("A registry already exists.")

        password = getpass.getpass(
            "Create your private access code: "
        )

        if len(password) < 16:
            raise ValueError(
                "Use at least 16 characters."
            )

        confirmation = getpass.getpass(
            "Confirm your access code: "
        )

        if password != confirmation:
            raise ValueError("Access codes do not match.")

        print("\nPaste your registry JSON below.")
        print("Finish with Ctrl+D (Linux/Mac) or Ctrl+Z (Windows).")

        raw_data = sys.stdin.read()
        registry = json.loads(raw_data)

        salt = os.urandom(16)
        key = self.derive_key(password, salt)

        encrypted = Fernet(key).encrypt(
            json.dumps(
                registry,
                ensure_ascii=False
            ).encode("utf-8")
        )

        payload = {
            "version": 1,
            "salt": base64.b64encode(salt).decode(),
            "ciphertext": encrypted.decode()
        }

        temporary = VAULT.with_suffix(".tmp")

        temporary.write_text(
            json.dumps(payload),
            encoding="utf-8"
        )

        os.chmod(temporary, 0o600)
        temporary.replace(VAULT)

        print("PHRINUSOMYIS registry encrypted.")

    def check_lockout(self):
        if not LOCKOUT.exists():
            return

        state = json.loads(
            LOCKOUT.read_text(encoding="utf-8")
        )

        remaining = (
            state["until"] - time.time()
        )

        if remaining > 0:
            raise PermissionError(
                f"Security lockout. Try again in "
                f"{int(remaining)} seconds."
            )

        LOCKOUT.unlink(missing_ok=True)

    def read_registry(self):
        self.check_lockout()

        if not VAULT.exists():
            raise FileNotFoundError("Registry not initialized.")

        payload = json.loads(
            VAULT.read_text(encoding="utf-8")
        )

        salt = base64.b64decode(payload["salt"])
        key = self.derive_key(
            getpass.getpass("Private access code: "),
            salt
        )

        try:
            decrypted = Fernet(key).decrypt(
                payload["ciphertext"].encode()
            )

        except InvalidToken:
            attempts = 1

            if LOCKOUT.exists():
                state = json.loads(
                    LOCKOUT.read_text()
                )
                attempts = state["attempts"] + 1

            if attempts >= MAX_ATTEMPTS:
                LOCKOUT.write_text(
                    json.dumps({
                        "attempts": attempts,
                        "until": time.time() + LOCKOUT_SECONDS
                    })
                )
            else:
                LOCKOUT.write_text(
                    json.dumps({
                        "attempts": attempts,
                        "until": 0
                    })
                )

            raise PermissionError(
                "ACCESS DENIED: Invalid access code."
            )

        LOCKOUT.unlink(missing_ok=True)

        return json.loads(decrypted.decode("utf-8"))

    def security_status(self):
        return {
            "organization": "PHRINUSOMYIS",
            "encryption": "Scrypt + Fernet",
            "authentication": "Required",
            "unauthorized_access": "Denied",
            "vault_exists": VAULT.exists()
        }


if __name__ == "__main__":

    security = PhrinusomyisSecureRegistry()

    if len(sys.argv) != 2:
        print("Commands: init | read | status")
        sys.exit(1)

    command = sys.argv[1]

    if command == "init":
        security.initialize()

    elif command == "read":
        print(json.dumps(
            security.read_registry(),
            indent=4,
            ensure_ascii=False
        ))

    elif command == "status":
        print(json.dumps(
            security.security_status(),
            indent=4
        ))

    else:
        print("Unknown command.")
