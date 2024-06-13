
//
document.addEventListener("DOMContentLoaded", function() {
    //variables form que toma el elemento registroForm
    var form = document.getElementById("registroForm");
    //primero quita el css hidden
    form.classList.remove('hidden');
    //luego lo muestra con el fade-in
    form.classList.add('fade-in-down');

    var formCard = form.querySelector(".card");
    var nextBtn = document.getElementById("nextBtn");
    var prevBtn = document.getElementById("prevBtn");

    nextBtn.addEventListener("click", function() {
        formCard.classList.add("flipped");
    });

    prevBtn.addEventListener("click", function() {
        formCard.classList.remove("flipped");
    });
});

// animations.js
document.addEventListener("DOMContentLoaded", function() {
    var elements = document.querySelectorAll('.hidden');
    elements.forEach(function(element) {
        element.classList.remove('hidden');
        element.classList.add('fade-in-down');
    });
});
//esconder navbar
document.addEventListener("mousemove", function(event) {
    var navbar = document.getElementById('navbar');
    if (event.clientY < 50) { // Si el ratón está en los primeros 50px de la pantalla
        navbar.classList.add('visible');
    } else {
        navbar.classList.remove('visible');
    }
});