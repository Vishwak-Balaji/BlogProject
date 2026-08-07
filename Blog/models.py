from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    titles = models.CharField(max_length=100)
    contents = models.TextField()
    img_urls = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self,*args,**kwargs):
        self.slug =slugify(self.titles)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.titles
