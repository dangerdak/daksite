from django.utils import timezone
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique_for_month='pub_date')
    body = models.TextField()
    category = models.ForeignKey(Category)

    DRAFT = 'DR'
    PUBLISH = 'PU'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISH, 'Publish'),
    ]
    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=DRAFT)

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.title
