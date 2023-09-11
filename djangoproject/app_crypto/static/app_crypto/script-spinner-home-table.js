
$("#market_data_table").hide();


$(document).ready(function () {

    setTimeout(() => {

        $("#spinner-box").show();

    }, 50);

    setTimeout(() => {

        var table = $('#market_data_table').DataTable({

            order: [[6, "desc"]],

            "ajax": {
                "url": "/home_table",
                "dataSrc": "",
                "dataType": "json",
                "className": "text-center",
                'processing': true,
                'serverSide': true,


            },
            "columns": [
                {
                    "data": "ticker"
                },

                {
                    "data": "name", render: function (data, type, row) {
                        return `<img " src="static/app_crypto/images/crypto_images/${row.ticker.toUpperCase()}.png" alt="Logo" width="30" height="30">  ${data} `
                    }
                },

                {
                    "data": "lastPrice", render: function (data, type) {

                        return $('#market_data_table').DataTable.render.number(',', '.', 2, '').display(data)
                    }
                },
                {
                    "data": "var_1h", render: function (data, type) {

                        if (data < 0) {
                            color = 'red';
                            var number = DataTable.render.number(',', '.', 2, '', '%').display(data);
                        }
                        else {
                            color = '#66FF00';
                            var number = DataTable.render.number(',', '.', 2, '+', '%').display(data);
                        }
                        return `<span style="color:${color}">${number}</span>`;

                    }

                },
                {
                    "data": "var_1d", render: function (data, type) {

                        if (data < 0) {
                            color = 'red';
                            var number = DataTable.render.number(',', '.', 2, '', '%').display(data);
                        }
                        else {
                            color = '#66FF00';
                            var number = DataTable.render.number(',', '.', 2, '+', '%').display(data);

                        }
                        return `<span style="color:${color}">${number}</span>`;
                    }
                },
                {
                    "data": "var_7d", render: function (data, type) {

                        if (data < 0) {
                            color = 'red';
                            var number = DataTable.render.number(',', '.', 2, '', '%').display(data);
                        }
                        else {
                            color = '#66FF00';
                            var number = DataTable.render.number(',', '.', 2, '+', '%').display(data);

                        }
                        return `<span style="color:${color}">${number}</span>`;
                    }
                },
                {
                    "data": "marketCap", render: function (data, type) {
                        return $('#market_data_table').DataTable.render.number(',', '.', 0, '').display(data)
                    }
                },
                {
                    "data": "volume24h", render: function (data, type) {
                        return $('#market_data_table').DataTable.render.number(',', '.', 0, '').display(data)
                    }
                },

            ],
            'columnDefs': [
                {
                    "targets": 1, // your case first column
                    "className": "text-left",
                    "targets": [0, 2, 3, 4, 5, 6, 7],
                    "className": "text-center",


                },

            ]

        });
        setInterval(function () {
            table.ajax.reload();
        }, 25000);

    }, 0);


    setTimeout(() => {

        $("#spinner-box").hide();

    }, 10000);

    setTimeout(() => {

        $("#market_data_table").show();

    }, 0);


});
