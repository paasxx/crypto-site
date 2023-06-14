# Generated by Django 4.2.1 on 2023-06-14 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ada",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "ADA",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "auth_group",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "auth_group_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codename", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "auth_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.BooleanField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.BooleanField()),
                ("is_active", models.BooleanField()),
                ("date_joined", models.DateTimeField()),
                ("first_name", models.CharField(max_length=150)),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "auth_user_groups",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "auth_user_user_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Avax",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "AVAX",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Bnb",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "BNB",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Btc",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "BTC",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Busd",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "BUSD",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Dai",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "DAI",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
                ("action_time", models.DateTimeField()),
            ],
            options={
                "db_table": "django_admin_log",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "django_content_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={
                "db_table": "django_migrations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "django_session",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Doge",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "DOGE",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Dot",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "DOT",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Etc",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "ETC",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Eth",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "ETH",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Hex",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "HEX",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Leo",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "LEO",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Ltc",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "LTC",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Matic",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "MATIC",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Shib",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "SHIB",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Sol",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "SOL",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Steth",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "STETH",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Trx",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "TRX",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Uni1",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "UNI1",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Usdc",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "USDC",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Usdt",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "USDT",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Wbtc",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "WBTC",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Wtrx",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "WTRX",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Xrp",
            fields=[
                (
                    "date",
                    models.TextField(
                        blank=True, db_column="Date", primary_key=True, serialize=False
                    ),
                ),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.IntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "XRP",
                "managed": False,
            },
        ),
    ]