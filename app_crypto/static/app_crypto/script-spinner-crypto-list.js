let jsondata = document.getElementById('crypto_data');
let json = JSON.parse(jsondata.textContent)
console.log(json);


$("#market_data_table").hide();

$(document).ready(function () {

    setTimeout(() => {

        $("#spinner-box").show();

    }, 50);

    setTimeout(() => {

        $.fn.dataTable.moment('DD/MM/YYYY');

        var table = $('#market_data_table').DataTable({

            data: json,

            columns: [

                {
                    "data": "date",
                    render: function (data, type, row) {
                        return moment(new Date(data).toString()).format('DD/MM/YYYY');
                    }

                },
                { "data": "open" },
                { "data": "high" },
                { "data": "low" },
                { "data": "close" },
                { "data": "adj_close" },
                { "data": "volume" },
            ],

        });

    }, 1000);

    setTimeout(() => {

        $("#spinner-box").hide();

    }, 750);

    setTimeout(() => {

        $("#market_data_table").show();

    }, 1000);




});
