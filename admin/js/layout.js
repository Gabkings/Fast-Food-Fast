function icon_bar() {
    var element = document.getElementById("myNavbar");
    if (element.className === "navbar") {
        element.className += " responsive";
    } else {
        element.className = "navbar";
    }
}


var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}