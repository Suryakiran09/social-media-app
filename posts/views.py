from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like, Comment
from .forms import PostForm, CommentForm

@login_required
def post_list(request):
    friends = request.user.profile.friends.all()
    posts = Post.objects.all().order_by('-created_at')
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form
    }
    return render(request, 'post_list.html', context)

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user.profile, post=post)
    if not created:
        like.delete()
    return redirect('post_list')

@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user.profile
            comment.post = post
            comment.save()
            return redirect('post_list')
    else:
        form = CommentForm()
    return redirect('post_list')