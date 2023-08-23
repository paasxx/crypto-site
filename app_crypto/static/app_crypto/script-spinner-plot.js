// let jsondata = document.getElementById('plot_crypto');
let footer = document.getElementById('footer');
// let json = JSON.parse(jsondata.textContent);
// console.log(jsondata)

$("#footer").hide();

$(document).ready(function () {

    setTimeout(() => {

        $("#spinner-box").show();

    }, 50);


    setTimeout(() => {

        $("#spinner-box").hide();

    }, 750);

    setTimeout(() => {

        $("#footer").show();

    }, 750);



});
