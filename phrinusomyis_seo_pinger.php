<?php
// Array of search engine ping URLs
$urls = [
    "https://www.google.com/ping?sitemap=https://phrinusomyis.com/sitemap.xml",
    "https://www.bing.com/ping?sitemap=https://phrinusomyis.com/sitemap.xml",
    "https://webmaster.yandex.com/site/map.xml?url=https://phrinusomyis.com/sitemap.xml"
];

foreach ($urls as $url) {
    // Initialize cURL session
    $ch = curl_init($url);

    // Return response instead of printing
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);

    // Execute request
    $response = curl_exec($ch);
    $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    // Check for errors
    if ($response === false) {
        echo "Error pinging $url: " . curl_error($ch) . "\n";
    } else {
        echo "$url -> HTTP Status Code: $httpcode\n";
    }

    // Close cURL session
    curl_close($ch);
}
?>
