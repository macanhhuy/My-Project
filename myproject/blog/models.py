from django.db import models
from django.db.models import permalink
from django.conf.locale import sl
from django.template.defaultfilters import slugify
import os
from filebrowser.fields import FileBrowseField

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Category(models.Model):
    title = models.CharField(max_length=80)
    slug = models.CharField(max_length=100,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if self.slug != "":
            super(Category, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.title)            
            super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
    @permalink
    def get_absolute_url(self):
        return "/category/%s/" % self.slug   
    
class Post(models.Model):
    title = models.CharField(max_length=80)
    slug = models.CharField(max_length=100,blank=True)
    thumbnail = FileBrowseField("Image", max_length=200, blank=True, null=True)
    category = models.ManyToManyField(Category)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
                            
        if self.slug != "":
            super(Post, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.title)            
            super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
    @permalink
    def get_absolute_url(self):
        return "/details/%s/" % self.slug 

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)
    def __unicode__(self):
        return u"%s: %s" % (self.post, self.body[:60])  