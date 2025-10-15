from django.db import models


class Post(models.Model):
    #author
    title = models.CharField(max_length=255)
    content = models.TextField()
    #image
    #category 
    counted_views = models.PositiveIntegerField(default=0)
    #tag
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title