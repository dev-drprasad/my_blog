from django import forms

from blog.models import Post
from blog.widgets import MarkdownEditor


class PostForm(forms.ModelForm):
    cover_image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ('title', 'slug', 'cover_image', 'content', 'is_draft')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post Title'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Slug to show in URL'}),
            'content': MarkdownEditor,
        }
