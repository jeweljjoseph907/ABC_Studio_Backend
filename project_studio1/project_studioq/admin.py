from django.contrib import admin
from .models import Contact, Esports
# Register your models here.
#class ContactAdmin(admin.ModelAdmin):
  #  list_display = ('name','email','message')
  #  search_fields = ('name','email', 'message')
  #  ordering = ('-id',)
admin.site.register(Contact)
admin.site.register(Esports)