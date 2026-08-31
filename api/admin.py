from django.contrib import admin
from .models import programmer

# Register your models here.
@admin.register(programmer)
class ProgrammerAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'nickname', 'language', 'age', 'is_active')
    list_filter = ('language', 'is_active')
    search_fields = ('fullname', 'nickname', 'language')
