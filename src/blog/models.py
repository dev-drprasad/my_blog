# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown2 as markdown
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import six
from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from .managers import AuthorManager


def avatar_path_handler(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    file_path = '{app_label}/{id}/avatar{ext}'.format(
        app_label=instance._meta.verbose_name, id=instance.id, ext=ext
    )
    abs_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(abs_path):
        os.remove(abs_path)
    return file_path


@python_2_unicode_compatible
class Author(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to=avatar_path_handler, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    website = models.URLField(max_length=200, blank=True, null=True)

    objects = AuthorManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]
    EMAIL_FIELD = 'email'

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    def __str__(self):
        return self.get_full_name() or self.username

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.avatar
            self.avatar = None
            super(Author, self).save(*args, **kwargs)
            self.avatar = saved_image

            # to avoid integrity error when force_insert=True
            kwargs['force_insert'] = False

        super(Author, self).save(*args, **kwargs)

    def clean(self):
        super(Author, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """

        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_staff(self):
        # Simplest possible answer: All users are staff
        return self.is_superuser


def upload_path_handler(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    file_path = '{app_label}/{id}/cover{ext}'.format(
        app_label=instance._meta.verbose_name, id=instance.id, ext=ext
    )
    abs_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(abs_path):
        os.remove(abs_path)
    return file_path


@python_2_unicode_compatible
class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class PostManager(models.Manager):
    def active(self):
        return super(PostManager, self).filter(publish=True)
        return super(PostManager, self).filter(publish=True)


@python_2_unicode_compatible
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    tags = models.ManyToManyField(Tag)
    cover_image = models.ImageField(upload_to=upload_path_handler, blank=True, null=True)
    content = models.TextField()
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    publish = models.BooleanField(default=True)

    objects = PostManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def content_as_html(self):
        """ Converts markdown syntax in content field to HTML"""
        return mark_safe(markdown.markdown(self.content, extras=["fenced-code-blocks"]))

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse('blog:post-detail', args=[self.slug])

    def cover_image_url(self):
        if self.cover_image and hasattr(self.cover_image, 'url'):
            return self.cover_image.url

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.cover_image
            self.cover_image = None
            super(Post, self).save(*args, **kwargs)
            self.cover_image = saved_image

            # to avoid integrity error when force_insert=True
            kwargs['force_insert'] = False

        super(Post, self).save(*args, **kwargs)
