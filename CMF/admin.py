from django.contrib import admin
from models import Organization, MoneyUser, Request

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin')
class MoneyUserAdmin(admin.ModelAdmin):
    list_display = ('money', 'owner')
class RequestAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'money', 'is_accept', 'is_fill',
                    'request_date')
admin.site.register(Organization,OrganizationAdmin)
admin.site.register(MoneyUser,MoneyUserAdmin)
admin.site.register(Request,RequestAdmin)