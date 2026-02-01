// Show the popup
document.getElementById("signin-icon").addEventListener("click", function () {
    const popup = document.getElementById("popup");
    popup.classList.add("show"); // Show popup
    popup.classList.remove("flip");
});

// Hide the popup on outside click
document.addEventListener("click", function (event) {
    const popup = document.getElementById("popup");
    if (!popup.contains(event.target) && event.target.id !== "signin-icon") {
        popup.classList.remove("show"); // Hide popup
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const popup = document.getElementById("popup");
    popup.classList.remove("hidden");
});

// Show login popup when the Sign-In icon is clicked
document.getElementById("signin-icon").addEventListener("click", function () {
    const popup = document.getElementById("popup");
    popup.classList.add("show"); // Show popup
    popup.classList.remove("flip"); // Ensure login is displayed
});

// Flip to show the Sign-Up form
document.getElementById("showSignup").addEventListener("click", function () {
    const popup = document.getElementById("popup");
    popup.classList.add("flip"); // Add flip effect
});

// Flip back to show the Login form
document.getElementById("showLogin").addEventListener("click", function () {
    const popup = document.getElementById("popup");
    popup.classList.remove("flip"); // Remove flip effect
});


