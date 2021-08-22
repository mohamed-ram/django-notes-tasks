from django.contrib import admin

from .forms import CategoryForm
from .models import Category



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'timestamp']
    form = CategoryForm
    
    def get_queryset(self, request):
        return Category.objects.filter(user=request.user)


admin.site.register(Category, CategoryAdmin)

