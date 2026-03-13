const eventDate = new Date('May 29, 2026 00:00:00').getTime();

function updateCountdown() {
    const now = new Date().getTime();
    const distance = eventDate - now;

    const d = Math.floor(distance / (1000 * 60 * 60 * 24));
    const h = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const m = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const s = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("countdown").innerHTML = d + "d " + h + "h " + m + "m " + s + "s ";

    if (distance < 0) {
        document.getElementById("countdown").innerHTML = "THE WORLD STAGE IS LIVE";
    }
}

setInterval(updateCountdown, 1000);
updateCountdown();

// Protection
document.addEventListener('dragstart', function(e) { if (e.target.nodeName === 'IMG') e.preventDefault(); });
