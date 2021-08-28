from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['username', 'id', 'useremail']
    
    def username(self, obj):
        return obj.user.username
    
    def useremail(self, obj):
        return obj.user.email


admin.site.register(Profile, ProfileAdmin)

