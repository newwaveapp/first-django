import math

from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class KidsTubeChannels(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False)
    address = models.CharField(max_length=100, null=False)
    rank = models.SmallIntegerField(unique=True, null=False)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.subject

    def get_page_count(self):
        count = self.posts.count()
        pages = count / 20
        return math.ceil(pages)

    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 6

    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, count + 1)

    def get_last_ten_posts(self):
        return self.posts.order_by('-created_at')[:10]

