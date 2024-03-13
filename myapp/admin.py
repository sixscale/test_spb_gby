from django.contrib import admin
from django.utils.safestring import mark_safe

from myapp.models import Event, Organization, User


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'get_image', 'date', ]
    search_fields = ['title', 'description', ]
    list_filter = ['date', 'organizations', ]
    readonly_fields = ['get_image', ]

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100px" height="80px"')

    get_image.short_description = 'Image'


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'address', 'postcode', ]
    search_fields = ['title', 'description', 'address', 'postcode', ]
    list_filter = ['title', 'address', 'postcode', ]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone_number', ]
    search_fields = ['email', 'phone_number', ]
    list_filter = ['email', 'phone_number', ]
