from django.conf import settings
from django.db import models
from django.utils import timezone

#학사일정
class Scheduler(models.Model):     
    titleList = models.CharField(max_length=100, blank=True)
    descriptionList = models.CharField(max_length=100, blank=True)
    cnt = models.IntegerField(unique=True, null=True)

    def set_lndex(self, i):
        self.cnt = i

class Job(models.Model):
    title = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100, blank=True)
    due = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=100, blank=True)

class Activity(models.Model):
    title = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100, blank=True)
    due = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=100, blank=True)

class Post(models.Model):
    author = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)