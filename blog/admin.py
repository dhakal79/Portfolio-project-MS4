from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category 


#@admin.register(Post)
admin.site.register(Post)
admin.site.register(Category)

class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body')
    
