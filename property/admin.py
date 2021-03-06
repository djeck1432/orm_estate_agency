from django.contrib import admin

from .models import Flat, Complain


class FlatdAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'owner_phone_pure']
    list_editable = ['new_building']
    list_filter = ['new_building', 'active', 'town']
    raw_id_fields = ['like']


class CompalinAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'complain_flat']


admin.site.register(Flat, FlatdAdmin)
admin.site.register(Complain, CompalinAdmin)

