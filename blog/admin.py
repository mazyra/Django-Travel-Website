from django.contrib import admin
from .models import Post

@admin.register(Post)    # admin.site.register(Post, PostAdmin)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_views', 'status', 'published_date', 'created_date')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    # fields = ('title',)
    # ordering = ['-created_date']



