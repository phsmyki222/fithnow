Const https = require('https');

const urls = [
    "https://www.google.com/ping?sitemap=https://phrinusomyis.com/sitemap.xml",
    "https://www.bing.com/ping?sitemap=https://phrinusomyis.com/sitemap.xml",
    "https://webmaster.yandex.com/site/map.xml?url=https://phrinusomyis.com/sitemap.xml"
];

urls.forEach(url => {
    https.get(url, res => {
        console.log(`${url} -> ${res.statusCode}`);
    }).on('error', e => {
        console.error(e);
    });
});


What name should I name this on my githup for active work
