from django import forms
from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=["post_description","post_image"]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']