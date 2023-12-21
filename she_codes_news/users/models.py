from django.db import models, transaction
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Abstract User is a default user (Authentication functionality)
class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    def delete(self, using=None, keep_parents=False):
        """ override the delete method on this model to allow for cleanup of relationships"""
        with transaction.atomic():
            # create a single transaction so that if something goes wrong
            # with any stage of the delete, then nothing will be deleted
            # to prevent half-deleting a user. 
            self.blog_post.all().delete()  # delete all of the items in the related many to many
            return super().delete(using=using, keep_parents=keep_parents)  # do the default delete