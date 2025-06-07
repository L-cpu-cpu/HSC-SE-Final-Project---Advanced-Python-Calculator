window.addEventListener("load", () => {
    const screen = document.getElementById("loading-screen");
    if (screen) {
    screen.style.animation = "fadeOut 2s ease forwards";
    setTimeout(() => {
        screen.style.display = "none";
    }, 2000); // Match extended animation duration
    }
});