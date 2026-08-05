from django.db import models

# Create your models here.
class Post(models.Model):
    titles = models.CharField(max_length=100)
    contents = models.TextField()
    img_urls = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titles
