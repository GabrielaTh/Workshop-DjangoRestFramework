from django.contrib import admin
from . import models
# Register your models here.



admin.site.register(models.Transports)
admin.site.register(models.TypeIncidents)
admin.site.register(models.Motivation)

@admin.register(models.Incidents)
class IncidentsAdmin(admin.ModelAdmin):
	list_display = ('nomIncident','idTypeIncidents')

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ("email","name","is_staff")

@admin.register(models.Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ("userId",)
    date_hierarchy = 'created'
    raw_id_fields = ["userId"]
    list_filter = ('userId', )

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("Business_key","company")

@admin.register(models.Periode)
class PeriodeAdmin(admin.ModelAdmin):
    list_display = ("session","is_Done")
    date_hierarchy = 'date'