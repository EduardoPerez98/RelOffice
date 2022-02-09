from django.contrib import admin

# Register your models here.
from gestion.models import Analistas, Oficios, Dependencias

admin.site.register(Analistas)
admin.site.register(Oficios)
admin.site.register(Dependencias)