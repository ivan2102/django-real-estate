from django.contrib import admin
from . models import Contacts

class ContactsAdmin(admin.ModelAdmin):
 list_display = ('id','name', 'email', 'phone', 'message')
 list_display_id = ('id', 'name')
 search_fields = ('name', 'email')
 list_per_page = 25

admin.site.register(Contacts, ContactsAdmin)
