from django.contrib import admin

from property.models import Complaint, Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address')
    readonly_fields = ["created_at"]
    list_display = ('address',
                    'price',
                    'owners_phonenumber',
                    'owner_pure_phone',
                    'new_building',
                    'construction_year',
                    'town')

    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('liked_by',)


admin.site.register(Flat, FlatAdmin)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('complainer', 'apartment',)


admin.site.register(Complaint, ComplaintAdmin)
