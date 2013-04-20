from django.db import models
from django.contrib import admin

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=60)
    email_address = models.EmailField()

    def __unicode__(self):
        return self.name

class Entry(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    update_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('Author')
    tags = models.ManyToManyField(Tag, related_name='entries')

    def __unicode__(self):
        return self.title

# Registe admin classes
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Entry)
