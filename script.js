/* PHRINUSOMYIS MASTER SCRIPT - ZERO ERROR VERSION */

// SET THE TARGET DATE: MAY 29, 2026
const targetDate = new Date("May 29, 2026 00:00:00").getTime();

function updateCountdowns() {
    const now = new Date().getTime();
    const distance = targetDate - now;

    // Time calculations for days, hours, minutes, and seconds
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Update all timer displays if they exist on the page
    const timers = ["timer1", "timer2", "timer3"];
    
    timers.forEach(id => {
        const element = document.getElementById(id);
        if (element) {
            element.innerHTML = ${days}d ${hours}h ${minutes}m ${seconds}s;
        }
    });

    // If the countdown is finished
    if (distance < 0) {
        clearInterval(timerInterval);
        const allTimers = document.querySelectorAll('[id^="timer"]');
        allTimers.forEach(t => t.innerHTML = "THE EVENT IS LIVE");
    }
}

// Run the timer every 1 second
const timerInterval = setInterval(updateCountdowns, 1000);

// Initialize immediately on load
updateCountdowns();

// Smooth Scroll for Navigation Links
document.querySelectorAll('header nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 70, // Adjusts for the fixed header height
                behavior: 'smooth'
            });
        }
    });
});

console.log("PHRINUSOMYIS System Online - All Systems Functional.");
