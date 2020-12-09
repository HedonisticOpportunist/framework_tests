let username = document.getElementById("username");
let password = document.getElementById("password");
let loginButton = document.getElementById("login-form-submit");
let loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();

    if (username.value === "user" && password.value === "holden") {
        window.location.href = "dashboard.html";
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})
