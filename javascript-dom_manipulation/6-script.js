fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")

.then(function (response) {
    return response.json();

})
.then(function (data) {

    let element = document.querySelector("#character");

    element.textContent = data.name;
});
