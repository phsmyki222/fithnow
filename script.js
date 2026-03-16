/* PHRINUSOMYIS MASTER SCRIPT */

const targetDate = new Date("May 29, 2026 00:00:00").getTime();

// Color configurations for specialized timers
const rainColors = [
    ['#FFD700', '#B8860B'], ['#FFFFFF', '#FFD700'], 
    ['#FF0000', '#8B0000'], ['#0000FF', '#00008B'], 
    ['#FFFF00', '#B8860B'], ['#00FF00', '#006400'], 
    ['#00FFFF', '#008B8B'], ['#FF00FF', '#8B008B']
];

const digitalColors = ["#FFD700", "#FF0000", "#00FF00", "#00FFFF", "#FFFFFF", "#FFA500", "#0000FF", "#FF00FF"];

function updateTimers() {
    const now = new Date().getTime();
    const gap = targetDate - now;

    // Select the DOM elements
    const t1 = document.getElementById('timer1');
    const t2 = document.getElementById('timer2');
    const t3 = document.getElementById('timer3');

    if (gap < 0) {
        const endedText = "THE WORLD STAGE IS OPEN";
        if(t1) t1.innerText = endedText;
        if(t2) t2.innerText = endedText;
        if(t3) t3.innerText = endedText;
        return;
    }

    // Time calculations
    const d = Math.floor(gap / (1000 * 60 * 60 * 24)).toString().padStart(2, '0');
    const h = Math.floor((gap % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)).toString().padStart(2, '0');
    const m = Math.floor((gap % (1000 * 60 * 60)) / (1000 * 60)).toString().padStart(2, '0');
    const s = Math.floor((gap % (1000 * 60)) / 1000).toString().padStart(2, '0');

    const fullStr = d + h + m + s; // 8-digit string for complex timers

    // 1. Gold Timer (Standard Text)
    if(t1) t1.innerText = `${d} : ${h} : ${m} : ${s}`;

    // 2. Rainbow Cinematic Timer (Top/Bottom Split)
    if(t3) {
        let rainHTML = "";
        fullStr.split('').forEach((char, i) => {
            const colors = rainColors[i % rainColors.length];
            rainHTML += `<span class="rainbow-digit" style="background-image: linear-gradient(to bottom, ${colors[0]} 50%, ${colors[1]} 50%)">${char}</span>`;
            if (i === 1 || i === 3 || i === 5) rainHTML += " : ";
        });
        t3.innerHTML = rainHTML;
    }

    // 3. Digital Multi-Color Timer
    if(t2) {
        let digiHTML = "";
        fullStr.split('').forEach((char, i) => {
            const color = digitalColors[i % digitalColors.length];
            digiHTML += `<span style="color: ${color}">${char}</span>`;
            if (i === 1 || i === 3 || i === 5) digiHTML += " : ";
        });
        t2.innerHTML = digiHTML;
    }
}

// Run the timer every second
setInterval(updateTimers, 1000);
updateTimers(); // Initial call
