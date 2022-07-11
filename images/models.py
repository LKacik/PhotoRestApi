from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return 'image/{0}'.format(filename)


class Category(models.Model):
    name = models.CharField(max_lenght=100)

    def __str__(self):
        return self.name


class Images(models.Model):

    option = (
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    alt = models.TextField(null=True)
    image = models.ImageField(
        upload_to=user_directory_path, default='post/default.jpg')
    slug = models.SlugField(max_length=250, unique_for_date='created')
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='author')
    status = models.CharField(max_length=11, choices=option, default='active')

