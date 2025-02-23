from django.contrib import admin
from .models import Complaint

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'priority', 'status')
    list_filter = ('priority', 'status')
    search_fields = ('name', 'email', 'product')

admin.site.register(Complaint, ComplaintAdmin)
