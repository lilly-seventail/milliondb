from django.contrib import admin
from .models import Idol

class IdolAdmin(admin.ModelAdmin):
    pass

admin.site.register(Idol)