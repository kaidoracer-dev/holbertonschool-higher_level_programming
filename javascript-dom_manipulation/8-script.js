document.addEventListener("DOMContentLoaded", function () {

    fetch("https://hellosalut.stefanbohacek.com/?lang=fr")

    .then(function(response) {
        return response.json();
    })

    .then(function(data) {

        let element = document.querySelector("#hello");

        element.textContent = data.hello;
    });
});
