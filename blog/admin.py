from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Comment


admin.site.register(Category)
admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
