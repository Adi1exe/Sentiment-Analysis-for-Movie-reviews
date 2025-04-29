        document.addEventListener("DOMContentLoaded", function () {

    if (localStorage.getItem("darkMode") === "enabled") {
        enableDarkMode();
    }

    document.getElementById("darkModeToggle").addEventListener("click", function () {
        if (document.body.classList.contains("bg-dark")) {
            disableDarkMode();
        } else {
            enableDarkMode();
        }
    });
});

function enableDarkMode() {
    document.body.classList.add("bg-dark", "text-white", "dark-mode");
    document.querySelectorAll(".form-control, .btn, .card").forEach(element => {
        element.classList.add("dark-mode-input");
    });
    localStorage.setItem("darkMode", "enabled");
    document.getElementById("darkModeToggle").innerText = "☀️";
}

function disableDarkMode() {
    document.body.classList.remove("bg-dark", "text-white", "dark-mode");
    document.querySelectorAll(".form-control, .btn, .card").forEach(element => {
        element.classList.remove("dark-mode-input");
    });
    localStorage.setItem("darkMode", "disabled");
    document.getElementById("darkModeToggle").innerText = "🌙";
}