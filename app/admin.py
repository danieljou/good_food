from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Repas)
admin.site.register(Menu)
admin.site.register(Commande)
admin.site.register(Table)