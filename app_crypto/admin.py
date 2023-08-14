from django.contrib import admin
from django.apps import apps

# Register your models here.
## Loop through all models names in app_crypto app.

models = apps.get_app_config("app_crypto").get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
