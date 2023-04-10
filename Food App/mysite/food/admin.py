from django.contrib import admin
from .models import Item
# Register your models here.

admin.site.site_header = 'Food App'
admin.site.site_title = 'Food App'
admin.site.index_title = 'Manage Food App'

admin.site.register(Item)