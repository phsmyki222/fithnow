// COUNTDOWN 1 – GOLD
function countdown1() {
    const targetDate = new Date("May 29, 2026 00:00:00").getTime();
    const countdownEl = document.getElementById("timer1");

    setInterval(() => {
        const now = new Date().getTime();
        const distance = targetDate - now;

        const days = Math.floor(distance / (1000*60*60*24));
        const hours = Math.floor((distance % (1000*60*60*24)) / (1000*60*60));
        const minutes = Math.floor((distance % (1000*60*60)) / (1000*60));
        const seconds = Math.floor((distance % (1000*60)) / 1000);

        countdownEl.innerHTML = <span style="color:#FFD700;">${days}d ${hours}h ${minutes}m ${seconds}s</span>;
    }, 1000);
}

// COUNTDOWN 2 – DIGITAL
function countdown2() {
    const targetDate = new Date("May 29, 2026 00:00:00").getTime();
    const countdownEl = document.getElementById("timer2");

    setInterval(() => {
        const now = new Date().getTime();
        const distance = targetDate - now;

        const days = Math.floor(distance / (1000*60*60*24));
        const hours = Math.floor((distance % (1000*60*60*24)) / (1000*60*60));
        const minutes = Math.floor((distance % (1000*60*60)) / (1000*60));
        const seconds = Math.floor((distance % (1000*60)) / 1000);

        countdownEl.innerHTML = <span style="color:red;">${days}</span>d <span style="color:blue;">${hours}</span>h <span style="color:white;">${minutes}</span>m <span style="color:yellow;">${seconds}</span>s;
    }, 1000);
}

// COUNTDOWN 3 – 4K CINEMATIC
function countdown3() {
    const targetDate = new Date("May 29, 2026 00:00:00").getTime();
    const countdownEl = document.getElementById("timer3");

    setInterval(() => {
        const now = new Date().getTime();
        const distance = targetDate - now;

        const days = Math.floor(distance / (1000*60*60*24));
        const hours = Math.floor((distance % (1000*60*60*24)) / (1000*60*60));
        const minutes = Math.floor((distance % (1000*60*60)) / (1000*60));
        const seconds = Math.floor((distance % (1000*60)) / 1000);

        countdownEl.innerHTML = <span style="color:#00FFFF;">${days}</span>d <span style="color:#FF00FF;">${hours}</span>h <span style="color:#FFFF00;">${minutes}</span>m <span style="color:#FF8C00;">${seconds}</span>s;
    }, 1000);
}

countdown1();
countdown2();
countdown3();
