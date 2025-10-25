from django.contrib import admin
from .models import Post, Category

@admin.register(Post)    # admin.site.register(Post, PostAdmin)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author','counted_views', 'status', 'published_date', 'created_date')
    list_filter = ('status','author')
    search_fields = ['title', 'content']
    # fields = ('title',)
    # ordering = ['-created_date']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


