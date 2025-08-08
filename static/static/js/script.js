function toggleNav() {
    var navLinks = document.getElementById("navLinks");
    if (navLinks.style.display === "flex") {
        navLinks.style.display = "none";
    } else {
        navLinks.style.display = "flex";
    }
}

function filterRecipes() {
    var input, filter, recipeList, tagSections, heading, i, j, txtValue;
    input = document.getElementById('search');
    filter = input.value.toLowerCase();
    recipeList = document.getElementById('recipe-tag-list');
    tagSections = recipeList.getElementsByClassName('tag-section');

    for (i = 0; i < tagSections.length; i++) {
        heading = tagSections[i].getElementsByTagName('h3')[0];
        if (heading) {
            txtValue = heading.textContent || heading.innerText;
            if (txtValue.toLowerCase().indexOf(filter) > -1) {
                tagSections[i].style.display = "";
            } else {
                tagSections[i].style.display = "none";
            }
        }
    }
}
