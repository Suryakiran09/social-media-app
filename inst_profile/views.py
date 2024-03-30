# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProfileForm
from .models import FriendRequest, Profile
from django.contrib.auth.models import User

@login_required(login_url='/login')
def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_form.html', {'form': form})

@login_required(login_url='/login')
def friends(request):
    profile = request.user.profile
    received_friend_requests = FriendRequest.objects.filter(to_user=profile, accepted=False)
    return render(request, 'friends.html', {'received_friend_requests': received_friend_requests})

@login_required
def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    users = users.exclude(profile__in=request.user.profile.friends.all())
    sent_friend_requests = FriendRequest.objects.filter(from_user=request.user.profile, accepted=False).values_list('to_user__id', flat=True)
    return render(request, 'user_list.html', {'users': users, 'sent_friend_requests': sent_friend_requests})

@login_required
def send_friend_request(request, user_id):
    from_user = request.user.profile
    to_user = get_object_or_404(Profile, user_id=user_id)
    friend_request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
    return redirect('user_list')

@login_required
def accept_friend_request(request, friend_request_id):
    friend_request = get_object_or_404(FriendRequest, id=friend_request_id)
    request.user.profile.accept_friend_request(friend_request)
    return redirect('friends')

@login_required
def reject_friend_request(request, friend_request_id):
    friend_request = get_object_or_404(FriendRequest, id=friend_request_id)
    request.user.profile.reject_friend_request(friend_request)
    return redirect('friends')

