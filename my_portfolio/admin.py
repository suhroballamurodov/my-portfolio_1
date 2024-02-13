from django.contrib import admin
from .models import *



class ContactAdmin(admin.ModelAdmin):
    list_display = ('ism', 'email', 'nomer','xabar')
    list_display_links = ('ism', )
    search_fields = ['ism','nomer']
    ordering = ['ism', 'nomer']


admin.site.register(ContactModel, ContactAdmin)


admin.site.site_title = "Admin panel"


# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'content','updated_at','created_at']
#     search_fields = ['title','content']
#     ordering = ['title','content']




# admin.site.register(Post,PostAdmin)