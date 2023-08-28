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
                {
                    "data": "open", render: function (data, type) {
                        if (data < 10) {
                            return $('#market_data_table').DataTable.render.number(',', '.', 15, '').display(data)
                        }
                        else { return $('#market_data_table').DataTable.render.number(',', '.', 2, '').display(data) }

                    }
                },
                {
                    "data": "high", render: function (data, type) {
                        if (data < 10) {
                            return $('#market_data_table').DataTable.render.number(',', '.', 15, '').display(data)
                        }
                        else { return $('#market_data_table').DataTable.render.number(',', '.', 2, '').display(data) }

                    }
                },
                {
                    "data": "low", render: function (data, type) {
                        if (data < 10) {
                            return $('#market_data_table').DataTable.render.number(',', '.', 15, '').display(data)
                        }
                        else { return $('#market_data_table').DataTable.render.number(',', '.', 2, '').display(data) }

                    }
                },
                {
                    "data": "close", render: function (data, type) {
                        if (data < 10) {
                            return $('#market_data_table').DataTable.render.number(',', '.', 15, '').display(data)
                        }
                        else { return $('#market_data_table').DataTable.render.number(',', '.', 2, '').display(data) }

                    }
                },
                {
                    "data": "adj_close", render: function (data, type) {
                        if (data < 10) {
                            return $('#market_data_table').DataTable.render.number(',', '.', 15, '').display(data)
                        }
                        else { return $('#market_data_table').DataTable.render.number(',', '.', 2, '').display(data) }

                    }
                },
                {
                    "data": "volume", render: function (data, type) {
                        if (data < 10) {
                            return $('#market_data_table').DataTable.render.number(',', '.', 15, '').display(data)
                        }
                        else { return $('#market_data_table').DataTable.render.number(',', '.', 2, '').display(data) }

                    }
                },
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




    }, 800);

    setTimeout(() => {

        $("#spinner-box").hide();

    }, 750);

    setTimeout(() => {

        $("#market_data_table").show();
        $("#footer").show();

    }, 800);




});
