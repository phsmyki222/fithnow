<?php
/**
 * PHRINUSOMYIS - Secure Transmission Gateway
 * Direction: Form -> Private Inbox (phrinusomyisllc@gmail.com)
 * No Database Storage: Absolute Data Privacy
 */

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // 1. Sanitize and Collect Identity & Email
    $identity = strip_tags(trim($_POST["identity"]));
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    
    // 2. Combine Country Code and Phone Number
    $countryCode = isset($_POST["countryCode"]) ? strip_tags(trim($_POST["countryCode"])) : "";
    $phoneNumber = isset($_POST["phone"]) ? strip_tags(trim($_POST["phone"])) : "";
    $fullPhone = $countryCode . " " . $phoneNumber;

    // 3. Sanitize Message
    $message = strip_tags(trim($_POST["message"]));

    // 4. Destination (Verified Address)
    $recipient = "phrinusomyisllc@gmail.com";
    $subject = "NEW CORPORATE TRANSMISSION: " . $identity;

    // 5. Construct Email Body
    $email_content = "---- PHRINUSOMYIS SECURE LIAISON ----\n\n";
    $email_content .= "SUBMITTER IDENTITY: $identity\n";
    $email_content .= "ENCRYPTED RETURN PATH: $email\n";
    $email_content .= "TELEPHONE: $fullPhone\n\n";
    $email_content .= "MESSAGE PAYLOAD:\n$message\n\n";
    $email_content .= "--------------------------------------\n";
    $email_content .= "Source: Universal Gateway Transmission\n";

    // 6. Headers
    $headers = "From: PHRINUSOMYIS Corporate <noreply@phrinusomyis.com>\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion();

    // 7. Execute Transmission
    if (mail($recipient, $subject, $email_content, $headers)) {
        http_response_code(200);
        echo "Transmission Secure.";
    } else {
        http_response_code(500);
        echo "Transmission Interrupted.";
    }

} else {
    http_response_code(403);
    echo "Access Denied.
    ";
}
?>
