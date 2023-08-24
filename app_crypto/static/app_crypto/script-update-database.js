


$("#spinner-box").hide();

setTimeout(() => {

    $("#teste").fadeOut(1200);

}, 4000);


function redirect_update_database() {

    $(".modal-content").hide();

    setTimeout(() => {

        $("#spinner-box").show();

    }, 50);

    window.location.href = "/update/";



}

