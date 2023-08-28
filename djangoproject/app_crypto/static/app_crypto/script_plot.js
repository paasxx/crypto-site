let selection = document.querySelector('select');


function redirect_crypto_page() {

    text = selection.options[selection.selectedIndex].text;
    text_upper_first = text.charAt(0).toUpperCase() + text.slice(1).toLocaleLowerCase();

    window.location.href = "/plot/" + text_upper_first

}