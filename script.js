/**
 * PHRINUSOMYIS MASTER LOGIC FILE
 * Version: 1.0 (Year 3001/6001 Precision)
 * Features: Gold Countdown Engine, 360° Asset Management, Security Locks
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // --- 1. MAY 2026 GOLD COUNTDOWN ENGINE ---
    const targetDate = new Date("May 1, 2026 00:00:00").getTime();

    function updateTimers() {
        const now = new Date().getTime();
        const distance = targetDate - now;

        // Time calculations
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Format: 00d / 00h / 00m / 00s
        const displayString = `${String(days).padStart(2, '0')}d / ${String(hours).padStart(2, '0')}h / ${String(minutes).padStart(2, '0')}m / ${String(seconds).padStart(2, '0')}s`;
        const digitalString = `${String(days).padStart(2, '0')} : ${String(hours).padStart(2, '0')} : ${String(minutes).padStart(2, '0')} : ${String(seconds).padStart(2, '0')}`;

        // Inject into Blueprint Sections
        // Section #countdown1 (Gold)
        const goldTimer = document.querySelector('#countdown1 .timer-display');
        if (goldTimer) goldTimer.innerText = displayString;

        // Section #countdown3 (Rainbow) & #countdown2 (Multi-color)
        const rainbowTimer = document.querySelector('#countdown3 .timer-display');
        if (rainbowTimer) rainbowTimer.innerText = digitalString;

        const multiTimer = document.querySelectorAll('#countdown2 .timer-display span');
        if (multiTimer.length === 4) {
            multiTimer[0].innerText = String(days).padStart(2, '0');
            multiTimer[1].innerText = String(hours).padStart(2, '0');
            multiTimer[2].innerText = String(minutes).padStart(2, '0');
            multiTimer[3].innerText = String(seconds).padStart(2, '0');
        }
    }

    // Run timer every second
    setInterval(updateTimers, 1000);
    updateTimers();

    // --- 2. 360° INTERACTIVE ROTATION (MOBILE FRIENDLY) ---
    // This allows the user to "spin" the assets with their finger or mouse
    const rotateAssets = document.querySelectorAll('.rotating-asset, .rotate-360');
    
    rotateAssets.forEach(asset => {
        let isDragging = false;
        let startX;
        let currentRotation = 0;

        asset.addEventListener('mousedown', (e) => {
            isDragging = true;
            startX = e.pageX;
        });

        window.addEventListener('mouseup', () => { isDragging = false; });

        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            const x = e.pageX;
            const walk = (x - startX) * 0.5; // Sensitivity
            asset.style.transform = `rotateY(${currentRotation + walk}deg)`;
        });

        // Touch support for Mobile
        asset.addEventListener('touchstart', (e) => {
            startX = e.touches[0].pageX;
            isDragging = true;
        });

        asset.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            const x = e.touches[0].pageX;
            const walk = (x - startX) * 0.5;
            asset.style.transform = `rotateY(${currentRotation + walk}deg)`;
        });

        asset.addEventListener('touchend', () => { isDragging = false; });
    });

    // --- 3. 12K VIEW: SMOOTH SCROLL & ENTRANCE ---
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            document.querySelector(targetId).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // --- 4. SECURITY & ASSET PROTECTION ---
    // Disabling right-click is already in the HTML, but this doubles the security
    document.addEventListener('contextmenu', (e) => {
        if (e.target.tagName === 'IMG' || e.target.tagName === 'VIDEO') {
            e.preventDefault();
        }
    }, false);

    // Stop users from dragging images off the site
    document.querySelectorAll('img').forEach(img => {
        img.addEventListener('dragstart', (e) => e.preventDefault());
    });

});
