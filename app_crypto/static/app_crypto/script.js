let selection = document.querySelector('select');
let result = document.querySelector("#teste");

selection.addEventListener('click', () => {
    result.innerText = selection.options[selection.selectedIndex].value;
});
