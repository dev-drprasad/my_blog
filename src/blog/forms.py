from django import forms

from blog.models import Post
from blog.widgets import MarkdownEditor


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'is_draft')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post Title'}),
            'content': MarkdownEditor,
        }