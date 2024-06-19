from django.contrib import admin
from formapp.models import * 

# Register your models here.
class mainAdmin(admin.ModelAdmin):
    list_display=('username','clinicid','domainname')
admin.site.register(main,mainAdmin)

