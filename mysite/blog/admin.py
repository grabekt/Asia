from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('tytul','autor','publikowany','utworzony','edytowany')
    search_fields = ('tytul', 'tekst')
    list_filter = ('autor', 'tytul','publikowany')
    ordering = ('publikowany',)
    
admin.site.register(Post, PostAdmin)
