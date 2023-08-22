let jsondata = document.getElementById('crypto_data');
let footer = document.getElementById('footer');
let json = JSON.parse(jsondata.textContent);

$("#market_data_table").hide();
$("#footer").hide();

$(document).ready(function () {

    setTimeout(() => {

        $("#spinner-box").show();

    }, 50);

    setTimeout(() => {

        $.fn.dataTable.moment('DD/MM/YYYY');


        var table = $('#market_data_table').DataTable({

            data: json,

            order: [[0, "desc"]],


            columns: [

                {
                    "data": "date",
                    render: function (data, type, row) {
                        return moment.utc(new Date(data).toUTCString()).format('DD/MM/YYYY');

                    }

                },
                { "data": "open" },
                { "data": "high" },
                { "data": "low" },
                { "data": "close" },
                { "data": "adj_close" },
                { "data": "volume" },
            ],
            dom: 'Bfrtip',
            lengthMenu: [
                [10, 25, 50, -1],
                ['10 rows', '25 rows', '50 rows', 'Show all']
            ],
            buttons: [
                {
                    extend: 'colvis',
                    collectionTitle: 'Column visibility control'

                },
                'pageLength',
                'copyHtml5',
                'excelHtml5',
                'csvHtml5',
                'pdfHtml5'
            ],
        });




    }, 1000);

    setTimeout(() => {

        $("#spinner-box").hide();

    }, 750);

    setTimeout(() => {

        $("#market_data_table").show();
        $("#footer").show();

    }, 1000);




});
