from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    # Fields to display in the user list
    list_display = ("username", "email", "phone_number", "is_staff", "is_active")
    
    # Fields in the add/change forms
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("phone_number",)}),  # Add phone_number in edit page
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("phone_number",)}),  # Add phone_number in create page
    )

# Register your models here.
admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)