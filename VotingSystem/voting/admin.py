
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser  # Import CustomUser from the users app

# Register the default User model
#admin.site.register(User, UserAdmin)

 

# custom user model

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')  # Customize fields to display

