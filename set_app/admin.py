from django.contrib import admin

from set_app.models import *

# Register your models here.

class ToDoadmin(admin.ModelAdmin):
    list_display = ('title', 'description', "send_at")


admin.site.register(ToDo, ToDoadmin)
admin.site.register(Delete)
admin.site.register(Izbran)


