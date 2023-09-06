
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

                'processing': true,
                'serverSide': true,


            },
            "columns": [
                {
                    "data": "ticker", render: function (data, type) {
                        return `<img src="{% static 'app_crypto/images/crypto_images/${data.toUpperCase()}.png' %}" alt="Logo" width="30" height="30">${data}`
                    }
                },

                { "data": "name" },

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

        });
        setInterval(function () {
            table.ajax.reload();
        }, 70000);

    }, 1000);


    setTimeout(() => {

        $("#spinner-box").hide();

    }, 750);

    setTimeout(() => {

        $("#market_data_table").show();

    }, 1000);


});
