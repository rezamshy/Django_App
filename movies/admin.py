from django.contrib import admin
from . import models

# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.models, MoviesAdmin)