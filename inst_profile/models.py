from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField(null=True,blank=True)
    photo = models.ImageField(upload_to='profile_photos', null=True, blank=True)
    friends = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.username

    def send_friend_request(self, to_user):
        friend_request, created = FriendRequest.objects.get_or_create(
            from_user=self, to_user=to_user
        )
        return friend_request

    def accept_friend_request(self, friend_request):
        if friend_request.to_user == self:
            friend_request.accepted = True
            friend_request.save()
            self.friends.add(friend_request.from_user)
            friend_request.from_user.friends.add(self)

    def reject_friend_request(self, friend_request):
        if friend_request.to_user == self:
            friend_request.delete()
            
class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        Profile, related_name='sent_friend_requests', on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        Profile, related_name='received_friend_requests', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f"Friend request from {self.from_user.username} to {self.to_user.username}"