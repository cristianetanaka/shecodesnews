from django.db import  models
from django.contrib.auth import get_user_model 


User = get_user_model()

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="stories"
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    
    class Meta:
        ordering = ['-pub_date'] 

    def __str__(self):
        return self.title