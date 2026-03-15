/**
 * PHRINUSOMYIS - Elite Production Logic
 * Handles 3 Different Countdown Styles and SEO Metadata
 */

// 1. Target Date: May 29, 2026
const targetDate = new Date("May 29, 2026 00:00:00").getTime();

// 2. Color Mapping for Countdown 3 (Rainbow Cinematic)
const rainbowColors = [
    ["#FF0000", "#0000FF"], // Digit 1: Red/Blue
    ["#FFA500", "#008000"], // Digit 2: Orange/Green
    ["#FFFF00", "#800080"], // Digit 3: Yellow/Purple
    ["#FF69B4", "#00FFFF"], // Digit 4: Pink/Cyan
    ["#FF00FF", "#00FF00"], // Digit 5: Magenta/Lime
    ["#4B0082", "#008080"], // Digit 6: Indigo/Teal
    ["#EE82EE", "#800000"], // Digit 7: Violet/Maroon
    ["#FFD700", "#000080"]  // Digit 8: Gold/Navy
];

// 3. Color Mapping for Countdown 2 (Digital Multi-Color)
const digitalColors = [
    "#FF0000", "#0000FF", "#008000", "#FFFF00", 
    "#FFA500", "#800080", "#00FFFF", "#FF00FF"
];

function updateCountdowns() {
    const now = new Date().getTime();
    const distance = targetDate - now;

    // Time calculations
    const d = Math.floor(distance / (1000 * 60 * 60 * 24)).toString().padStart(2, '0');
    const h = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)).toString().padStart(2, '0');
    const m = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)).toString().padStart(2, '0');
    const s = Math.floor((distance % (1000 * 60)) / 1000).toString().padStart(2, '0');

    // Combine into a single string of 8 digits
    const timeString = d + h + m + s;

    // --- COUNTDOWN 1: PURE GOLD ---
    const goldTimer = document.getElementById("timer1");
    if (goldTimer) {
        goldTimer.innerText = `${d} : ${h} : ${m} : ${s}`;
    }

    // --- COUNTDOWN 3: RAINBOW CINEMATIC (DUAL-COLOR SPLIT) ---
    const rainbowTimer = document.getElementById("timer3");
    if (rainbowTimer) {
        rainbowTimer.innerHTML = timeString.split('').map((char, i) => {
            return `<span class="rainbow-digit" style="background-image: linear-gradient(to bottom, ${rainbowColors[i][0]} 50%, ${rainbowColors[i][1]} 50%)">${char}</span>`;
        }).join('');
    }

    // --- COUNTDOWN 2: DIGITAL MULTI-COLOR ---
    const digitalTimer = document.getElementById("timer2");
    if (digitalTimer) {
        digitalTimer.innerHTML = timeString.split('').map((char, i) => {
            return `<span style="color: ${digitalColors[i]}; padding: 0 2px;">${char}</span>`;
        }).join('');
    }

    // Stop if countdown reaches zero
    if (distance < 0) {
        clearInterval(timerInterval);
        document.querySelectorAll('.timer-display').forEach(el => el.innerText = "LIVE NOW");
    }
}

// Update every second
const timerInterval = setInterval(updateCountdowns, 1000);

// Initialize immediately on load
window.onload = updateCountdowns;

/**
 * 4. RIGHT-CLICK DISABLE
 * To protect the "Sovereign" brand assets
 */
document.addEventListener('contextmenu', event => event.preventDefault());
