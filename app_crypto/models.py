from django.db import models

# Create your models here.


class Ada(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ADA"


class Avax(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "AVAX"


class Bnb(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "BNB"


class Btc(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase. This field type is a guess.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "BTC"


class Busd(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "BUSD"


class Dai(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "DAI"


class Doge(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "DOGE"


class Dot(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "DOT"


class Etc(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ETC"


class Eth(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase. This field type is a guess.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ETH"


class Hex(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "HEX"


class Leo(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "LEO"


class Ltc(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "LTC"


class Matic(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MATIC"


class Shib(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "SHIB"


class Sol(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "SOL"


class Steth(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "STETH"


class Trx(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "TRX"


class Uni1(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "UNI1"


class Usdc(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "USDC"


class Usdt(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "USDT"


class Wbtc(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "WBTC"


class Wtrx(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "WTRX"


class Xrp(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=False, primary_key=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "XRP"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"
