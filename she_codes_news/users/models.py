from django.db import models, transaction
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse
# Abstract User is a default user (Authentication functionality)
class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
   
    def delete(self, using=None, keep_parents=False):
        """
        Override the delete method to allow for cleanup of relationships.

        This method ensures that related blog posts are deleted before
        deleting the user to prevent partial deletion.
        """
        with transaction.atomic():
            self.blog_post.all().delete()
            super().delete(using=using, keep_parents=keep_parents)

    def get_absolute_url(self):
        return reverse('AccountView', args=[str(self.id)])