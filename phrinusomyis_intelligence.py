
import os
import json
import time
import base64
import shutil
import logging
from getpass import getpass
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


# ==================================================
# PHRINUSOMYIS™ PRIVATE INTELLIGENCE VAULT
# ==================================================

VAULT_FILE = Path("phrinusomyis_registry.enc")
BACKUP_FILE = Path("phrinusomyis_backup.enc")
LOG_FILE = Path("security_events.log")

MAGIC = b"PHRINUSOMYIS-VAULT-V1\n"
SALT_SIZE = 16

MAX_ATTEMPTS = 5
LOCKOUT_SECONDS = 900

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.WARNING,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class PhrinusomyisVault:

    def __init__(self):
        self.failed_attempts = 0
        self.locked_until = 0
        self.registry = None

    # ----------------------------------------------
    # PASSWORD KEY GENERATION
    # ----------------------------------------------

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

    # ----------------------------------------------
    # PASSWORD VALIDATION
    # ----------------------------------------------

    def get_password(self):

        password = getpass("Enter private access password: ")

        if len(password) < 16:
            raise ValueError(
                "Password must contain at least 16 characters."
            )

        return password

    # ----------------------------------------------
    # ENCRYPTED STORAGE
    # ----------------------------------------------

    def save_registry(self, registry, password):

        salt = os.urandom(SALT_SIZE)

        key = self.derive_key(password, salt)

        cipher = Fernet(key)

        data = json.dumps(
            registry,
            ensure_ascii=False,
            indent=4
        ).encode("utf-8")

        encrypted_data = cipher.encrypt(data)

        if VAULT_FILE.exists():
            shutil.copy2(VAULT_FILE, BACKUP_FILE)

        temporary_file = VAULT_FILE.with_suffix(".tmp")

        with open(temporary_file, "wb") as file:
            file.write(MAGIC + salt + encrypted_data)

        os.replace(temporary_file, VAULT_FILE)

        self.set_permissions(VAULT_FILE)

        logging.info("Encrypted registry saved.")

    # ----------------------------------------------
    # SECURE RETRIEVAL
    # ----------------------------------------------

    def load_registry(self, password):

        if not VAULT_FILE.exists():
            raise FileNotFoundError(
                "Encrypted registry does not exist."
            )

        raw = VAULT_FILE.read_bytes()

        if not raw.startswith(MAGIC):
            raise ValueError("Invalid vault format.")

        offset = len(MAGIC)

        salt = raw[offset:offset + SALT_SIZE]

        encrypted_data = raw[offset + SALT_SIZE:]

        key = self.derive_key(password, salt)

        cipher = Fernet(key)

        decrypted = cipher.decrypt(encrypted_data)

        return json.loads(decrypted.decode("utf-8"))

    # ----------------------------------------------
    # FILE PERMISSIONS
    # ----------------------------------------------

    def set_permissions(self, path):

        try:
            if os.name != "nt":
                os.chmod(path, 0o600)
        except OSError:
            logging.warning("Could not change file permissions.")

    # ----------------------------------------------
    # ACCESS MONITORING
    # ----------------------------------------------

    def check_access(self):

        if time.time() < self.locked_until:
            remaining = int(self.locked_until - time.time())

            print(
                f"ACCESS LOCKED. Try again in {remaining} seconds."
            )

            return False

        return True

    def failed_access(self):

        self.failed_attempts += 1

        logging.warning("Failed vault authentication attempt.")

        if self.failed_attempts >= MAX_ATTEMPTS:

            self.locked_until = time.time() + LOCKOUT_SECONDS

            self.failed_attempts = 0

            logging.critical(
                "Temporary access lock activated."
            )

            print("SECURITY LOCK ACTIVATED.")

    # ----------------------------------------------
    # INITIALIZE VAULT
    # ----------------------------------------------

    def initialize(self):

        if VAULT_FILE.exists():
            print("An encrypted vault already exists.")
            return

        print("\nPHRINUSOMYIS™ VAULT INITIALIZATION")
        print("----------------------------------")
        print("Paste your registry information as JSON.")
        print("Enter END on a separate line when finished.\n")

        lines = []

        while True:
            line = input()

            if line.strip() == "END":
                break

            lines.append(line)

        try:
            registry = json.loads("\n".join(lines))

            if not isinstance(registry, dict):
                raise ValueError("Registry must be a JSON object.")

        except (json.JSONDecodeError, ValueError) as error:
            print("Invalid registry:", error)
            return

        password = self.get_password()

        confirmation = getpass("Confirm access password: ")

        if password != confirmation:
            print("Passwords do not match.")
            return

        self.save_registry(registry, password)

        print("\nENCRYPTED VAULT CREATED SUCCESSFULLY.")

    # ----------------------------------------------
    # AUTHENTICATION
    # ----------------------------------------------

    def authenticate(self):

        if not self.check_access():
            return False

        for _ in range(MAX_ATTEMPTS):

            if not self.check_access():
                return False

            try:
                password = getpass("Private access code: ")

                self.registry = self.load_registry(password)

                self.failed_attempts = 0

                logging.info("Authorized vault access.")

                print("\nACCESS AUTHORIZED.")

                return True

            except InvalidToken:
                print("ACCESS DENIED.")
                self.failed_access()

            except (ValueError, OSError, json.JSONDecodeError):
                logging.error("Vault access or integrity error.")
                print("VAULT ACCESS FAILED.")
                return False

        return False

    # ----------------------------------------------
    # AUTHORIZED INFORMATION DISPLAY
    # ----------------------------------------------

    def view_registry(self):

        if self.registry is None:
            print("ACCESS DENIED.")
            return

        print("\nPHRINUSOMYIS™ PRIVATE REGISTRY")
        print("--------------------------------")

        print(json.dumps(
            self.registry,
            ensure_ascii=False,
            indent=4
        ))

    # ----------------------------------------------
    # UPDATE REGISTRY
    # ----------------------------------------------

    def update_registry(self, password):

        print("\nPaste the replacement registry JSON.")
        print("Enter END on a separate line when finished.\n")

        lines = []

        while True:
            line = input()

            if line.strip() == "END":
                break

            lines.append(line)

        try:
            updated = json.loads("\n".join(lines))

            if not isinstance(updated, dict):
                raise ValueError("Registry must be a JSON object.")

            self.save_registry(updated, password)

            self.registry = updated

            print("REGISTRY UPDATED AND ENCRYPTED.")

        except (json.JSONDecodeError, ValueError) as error:
            print("Update rejected:", error)

    # ----------------------------------------------
    # MAIN INTERFACE
    # ----------------------------------------------

    def run(self):

        print("=" * 50)
        print("PHRINUSOMYIS™ PRIVATE INTELLIGENCE")
        print("ENCRYPTED REGISTRY PROTECTION")
        print("=" * 50)

        if not VAULT_FILE.exists():
            self.initialize()
            return

        if not self.authenticate():
            print("UNAUTHORIZED ACCESS DENIED.")
            return

        # Keep password in memory only while session is active.
        password = getpass("Re-enter password for management: ")

        try:
            self.load_registry(password)
        except InvalidToken:
            print("MANAGEMENT AUTHENTICATION FAILED.")
            return

        while True:

            print("\n1. View protected registry")
            print("2. Update protected registry")
            print("3. Exit and lock vault")

            choice = input("\nSelect operation: ").strip()

            if choice == "1":
                self.view_registry()

            elif choice == "2":
                self.update_registry(password)

            elif choice == "3":
                self.registry = None
                password = None
                print("VAULT LOCKED.")
                break

            else:
                print("Invalid selection.")


# ==================================================
# START SECURITY SYSTEM
# ==================================================

if __name__ == "__main__":

    vault = PhrinusomyisVault()

    try:
        vault.run()

    except KeyboardInterrupt:
        vault.registry = None
        print("\nVAULT SESSION CLOSED.")
