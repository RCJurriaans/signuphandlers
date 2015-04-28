from django.contrib import admin
from codecultform.models import SummerSchoolSignUp

class SSAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'age', 'message',)
    list_filter = ('city',)

# Register your models here.
admin.site.register(SummerSchoolSignUp, SSAdmin)
