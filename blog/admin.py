from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Comment

@admin.register(Post)    # admin.site.register(Post, PostAdmin)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status', 'login_require', 'published_date', 'created_date')
    list_filter = ('status','author')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
    # fields = ('title',)
    # ordering = ['-created_date']


@admin.register(Comment)    
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'subject', 'email', 'approved', 'updated_date', 'created_date')
    list_filter = ('name','approved')
    search_fields = ['name', 'message']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


