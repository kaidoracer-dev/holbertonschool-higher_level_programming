let button = document.querySelector("#add_item");

button.addEventListener("click", function () {
    
    let newItem = document.createElement("li");

    newItem.textContent = "Item";

    let list = document.querySelector(".my_list");

    list.appendChild(newItem);

});
