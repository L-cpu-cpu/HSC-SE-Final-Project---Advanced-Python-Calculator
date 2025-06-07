window.addEventListener("load", () => {
    const screen = document.getElementById("loading-screen");
    if (screen) {
    screen.style.animation = "fadeOut 1s ease forwards";
    setTimeout(() => {
        screen.style.display = "none";
    }, 1000); // Match extended animation duration
    }
});