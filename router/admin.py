from django.contrib import admin
from router.models import Router,Username
# Register your models here.
class RouterAdmin(admin.ModelAdmin):
    pass
class UsernameAdmin(admin.ModelAdmin):
    pass

admin.site.register(Router, RouterAdmin)
admin.site.register(Username, UsernameAdmin)




