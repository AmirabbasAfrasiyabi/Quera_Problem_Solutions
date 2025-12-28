from Users.models import Birthday
from django.contrib import admin

#from django_jalali.admin.filters import JDateFieldListFilter
#import django_jalali.admin as jadmin


admin.site.register(Birthday)

from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'gender', 'national_code', 'birthday_date')
    search_fields = ('username', 'full_name')
    ordering = ('ceremony_datetime',)

    def first_name(self, obj):
        return obj.get_first_and_last_name()['first_name']

    def last_name(self, obj):
        return obj.get_first_and_last_name()['last_name']
