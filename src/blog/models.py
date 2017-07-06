# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()

	def __unicode__(self):
		return self.title