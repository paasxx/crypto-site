let selection = document.querySelector('select');
let result_market_data = document.querySelector("#market_data");
let result_plot = document.querySelector("#plot");



selection.addEventListener('change', () => {
    result_market_data.innerText = selection.options[selection.selectedIndex].text;
    result_market_data.href = "market_data/" + selection.options[selection.selectedIndex].text.charAt(0).toUpperCase() + selection.options[selection.selectedIndex].text.slice(1).toLocaleLowerCase();
    result_plot.innerText = selection.options[selection.selectedIndex].text;
    result_plot.href = "plot/" + selection.options[selection.selectedIndex].text.charAt(0).toUpperCase() + selection.options[selection.selectedIndex].text.slice(1).toLocaleLowerCase();

});

