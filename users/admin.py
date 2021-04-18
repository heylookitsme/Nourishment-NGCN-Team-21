from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import Group
from .forms import (
    AdminUserUpdateForm,AdminUserCreateForm
    )

class UserAdmin(BaseUserAdmin):
    form = AdminUserUpdateForm
    add_form = AdminUserCreateForm
    list_display = ('email','username','location','active','staff','superuser')
    list_filter = ('superuser','staff','active')
    fieldsets = (
        (None , {'fields':('username','email','location','password')}),
        ('permissions',{'fields':('active','staff','superuser')}),
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','username','password1','password2')
        }),
        ('permissions',{
            'classes':('wide',),
            'fields':('active','staff','superuser')
        }),                
    )
    search_fields = ('email','username','location',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User,UserAdmin)

admin.site.unregister(Group)