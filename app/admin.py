from django.contrib import admin
from app.models import register_table,appointment
admin.site.site_header="MEDC"
admin.site.register(register_table)
admin.site.register(appointment)
