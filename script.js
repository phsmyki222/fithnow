/**
 * PHRINUSOMYIS Official Terminal Logic
 * Target Launch: May 1, 2026
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Set the Target Date (May 2026)
    const launchDate = new Date("May 1, 2026 00:00:00").getTime();

    function updateAllCountdowns() {
        const now = new Date().getTime();
        const distance = launchDate - now;

        // Time calculations
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Map to the different IDs in your HTML
        const timeData = {
            d: days.toString().padStart(2, '0'),
            h: hours.toString().padStart(2, '0'),
            m: minutes.toString().padStart(2, '0'),
            s: seconds.toString().padStart(2, '0')
        };

        // Update Countdown 1 (Gold)
        updateElement('d1', timeData.d);
        updateElement('h1', timeData.h);
        updateElement('m1', timeData.m);
        updateElement('s1', timeData.s);

        // Update Countdown 2 (Multi-color)
        updateElement('d2', timeData.d);
        updateElement('h2', timeData.h);
        updateElement('m2', timeData.m);
        updateElement('s2', timeData.s);

        // Update Countdown 3 (Rainbow)
        updateElement('d3', timeData.d);
        updateElement('h3', timeData.h);
        updateElement('m3', timeData.m);
        updateElement('s3', timeData.s);

        // If the countdown is finished
        if (distance < 0) {
            clearInterval(timerInterval);
            document.querySelectorAll('.timer-display').forEach(el => {
                el.innerHTML = "EVENT LIVE";
            });
        }
    }

    function updateElement(id, value) {
        const el = document.getElementById(id);
        if (el) el.innerText = value;
    }

    // Run every second
    const timerInterval = setInterval(updateAllCountdowns, 1000);
    updateAllCountdowns(); // Initial call

    // 2. Global Security: Disable Right-Click on Media
    document.addEventListener('contextmenu', (e) => {
        if (e.target.tagName === 'IMG' || e.target.tagName === 'VIDEO') {
            e.preventDefault();
        }
    }, false);

    // 3. Smooth Scroll for Navigation
    document.querySelectorAll('.nav-menu a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const section = document.querySelector(this.getAttribute('href'));
            if (section) {
                section.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

});
