# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Server(models.Model):
	name = models.CharField(max_length=200)
	details = models.TextField(blank=True)
	created_at = models.DateTimeField(default=timezone.now)
	# updated_date = models.DateTimeField(blank=True, null=True)

	# def update(self):
	# 	self.updated_date = timezone.now()
	# 	self.save()

	def __str__(self):
		return self.name