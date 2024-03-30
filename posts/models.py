from django.db import models
from django.contrib.auth.models import User
from inst_profile.models import Profile
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    post_description = models.CharField(max_length=500, blank=True, null=True)
    post_image = models.ImageField(upload_to='posts')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_description

class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} liked {self.post.post_description}"
    
class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.CharField(max_length= 50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} commented on {self.post.post_description}"