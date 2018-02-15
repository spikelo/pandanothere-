from django.contrib import admin
from .models import Profile
from router.models import Username,Router

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname' , 'patronymic', 'contact_number' ,'manager','colored_status',)
    list_filter = ('manager','status', 'date_creating', 'prefering_connection',)
    list_per_page = 50
    search_fields = ('^name','^surname', '^patronymic', '^address', '^flat', '^home', '^contact_number','^manager__username')


admin.site.register(Profile, ProfileAdmin)
