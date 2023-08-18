let selection = document.querySelector('select');
let result_crypto_list = document.querySelector("#teste");




selection.addEventListener('change', () => {

    result_crypto_list.innerText = selection.options[selection.selectedIndex].text;
    result_crypto_list.href = selection.options[selection.selectedIndex].text.charAt(0).toUpperCase() + selection.options[selection.selectedIndex].text.slice(1).toLocaleLowerCase();

});

// function redirect_crypto_page() {

//     result_crypto_list.innerText = selection.options[selection.selectedIndex].text;
//     result_crypto_list.href = selection.options[selection.selectedIndex].text.charAt(0).toUpperCase() + selection.options[selection.selectedIndex].text.slice(1).toLocaleLowerCase();

//     window.location.href = "{% url'/market_data/Sol' %}"

// }