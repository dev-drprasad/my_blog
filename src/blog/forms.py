from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from blog.models import Post, Author
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


class AuthorForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(
        label="Password",
        help_text=
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"../password/\">this form</a>."
        ,
    )

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'email', 'website', 'is_active', 'avatar', 'about',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
