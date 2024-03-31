from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Message, Group
from inst_profile.models import Profile
from django.db.models import Count


@login_required
def chat(request):
    profile = request.user.profile
    friends = profile.friends.all()
    groups = profile.groups.all()
    individual_messages = Message.objects.filter(
        recipients=profile
    ).annotate(
        recipients_count=Count('recipients')
    ).filter(
        recipients_count=2
    ).order_by('-timestamp')
    group_messages = Message.objects.filter(
        recipients__in=profile.groups.values_list('members', flat=True)
    ).order_by('-timestamp')

    return render(request, 'chat.html', {
        'friends': friends,
        'groups': groups,
        'individual_messages': individual_messages,
        'group_messages': group_messages
    })
@login_required
def individual_chat(request, user_id):
    profile = request.user.profile
    friend = get_object_or_404(Profile, id=user_id)
    messages = Message.objects.filter(
        recipients__in=[profile, friend]
    ).order_by('-timestamp')

    return render(request, 'individual_chat.html', {
        'friend': friend,
        'messages': messages
    })
    
@login_required
def group_chat(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    messages = Message.objects.filter(
        recipients__in=group.members.all()
    ).order_by('-timestamp')

    return render(request, 'group_chat.html', {
        'group': group,
        'messages': messages
    })

@login_required
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        recipient_ids = request.POST.getlist('recipients')
        group_id = request.POST.get('group_id')
        sender = request.user.profile

        if group_id:
            group = get_object_or_404(Group, id=group_id)
            recipients = group.members.all()
            message = Message.objects.create(sender=sender, content=content)
            message.recipients.set(recipients)
            return redirect('group_chat', group_id=group.id)
        else:
            recipients = Profile.objects.filter(id__in=recipient_ids)
            message = Message.objects.create(sender=sender, content=content)
            message.recipients.set(recipients)
            if len(recipients) == 1:
                return redirect('individual_chat', user_id=recipients.first().id)
            else:
                return redirect('chat')

    return redirect('chat')

@login_required
def mark_message_read(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.user.profile in message.recipients.all():
        message.is_read = True
        message.save()
    return redirect('chat')

@login_required
def create_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        member_ids = request.POST.getlist('members')
        created_by = request.user.profile
        members = Profile.objects.filter(id__in=member_ids)
        group = Group.objects.create(name=name, created_by=created_by)
        group.members.set(members)

    return redirect('chat')