from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Comment


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)


class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
