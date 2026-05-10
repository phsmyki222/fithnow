<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and clean data
    $name = strip_tags(trim($_POST["name"])); 
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $message = strip_tags(trim($_POST["message"]));

    // Destination
    $recipient = "phrinusomyisllc@gmail.com";
    $subject = "New PHRINUSOMYIS Transmission";

    // Email Content
    $email_content = "New inquiry received:\n\n";
    $email_content .= "Name: $name\n";
    $email_content .= "Email: $email\n\n";
    $email_content .= "Message:\n$message\n";

    // Email Headers
    $headers = "From: $name <$email>";

    // Send the email
    if (mail($recipient, $subject, $email_content, $headers)) {
        http_response_code(200);
        echo "Success";
    } else {
        http_response_code(500);
        echo "Error";
    }
} else {
    http_response_code(403);
    echo "Direct access forbidden.";
}
?>
