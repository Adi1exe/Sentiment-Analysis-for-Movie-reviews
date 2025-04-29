async function fetchSuggestions() {
    const input = document.getElementById("movieTitle").value.trim();
    const suggestionsList = document.getElementById("suggestionsList");

    if (input.length < 2) {
        suggestionsList.style.display = "none";
        return;
    }

    try {
        const response = await fetch(`/suggest?query=${input}`);
        const data = await response.json();
        suggestionsList.innerHTML = "";

        if (Array.isArray(data)) {
            data.forEach(movie => {
                const listItem = document.createElement("li");
                listItem.classList.add("list-group-item", "list-group-item-action");
                listItem.textContent = `${movie.Title} (${movie.Year})`;
                listItem.onclick = () => {
                    document.getElementById("movieTitle").value = movie.Title;
                    suggestionsList.style.display = "none";
                };
                suggestionsList.appendChild(listItem);
            });
            suggestionsList.style.display = "block";
        } else {
            suggestionsList.style.display = "none";
        }
    } catch (error) {
        console.error("Error fetching suggestions:", error);
    }
}

document.addEventListener("click", function(event) {
    if (!document.getElementById("movieTitle").contains(event.target)) {
        document.getElementById("suggestionsList").style.display = "none";
    }
});
        async function fetchMovie() {
            const title = document.getElementById("movieTitle").value.trim();
            if (!title) return;

            const response = await fetch(`/movie?title=${title}`);
            const data = await response.json();

            const movieDiv = document.getElementById("movieDetails");

            if (data.error) {
                movieDiv.innerHTML = `<p class="text-danger text-center animate__animated animate__shakeX">${data.error}</p>`;
            } else {
                movieDiv.innerHTML = `
                    <div class="card shadow-lg border-0 animate__animated animate__zoomIn">
                        <div class="row g-0">
                            <div class="col-md-4">
                                <img src="${data.poster}" class="img-fluid rounded-start" alt="Movie Poster">
                            </div>
                            <div class="col-md-8">
                                <div class="card-body">
                                    <h5 class="card-title">${data.title} (${data.year})</h5>
                                    <p class="card-text"><strong>IMDb Rating:</strong> ⭐ ${data.imdb_rating}/10</p>
                                    <p class="card-text">${data.plot}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
            }
        }

    async function analyzeReview() {
    const review = document.getElementById("userReview").value.trim();
    if (!review) return;

    document.getElementById("loadingSpinner").style.display = "block";

    const response = await fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ review })
    });

    const result = await response.json();

    document.getElementById("loadingSpinner").style.display = "none";

    let sentimentText = result.sentiment;
    let bgColor, shadowColor;

    if (sentimentText === "Positive") {
        bgColor = "bg-success";
        shadowColor = "rgba(0, 255, 0, 0.6)";
    } else if (sentimentText === "Negative") {
        bgColor = "bg-danger";
        shadowColor = "rgba(255, 0, 0, 0.6)";
    } else {
        bgColor = "bg-secondary";
        shadowColor = "rgba(128, 128, 128, 0.6)";
    }

    document.getElementById("sentimentResult").innerHTML = `
        <div class="sentiment-box ${bgColor} text-white animate__animated animate__bounceIn">
            <span>Sentiment: ${sentimentText}</span>
        </div>
    `;
    
    document.querySelector('.sentiment-box').style.boxShadow = `0 0 20px ${shadowColor}`;
}


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