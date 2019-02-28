# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.contrib import admin

class ServiceDT(models.Model):
	name = models.CharField(max_length=150)
	url = models.URLField()
	stype = models.CharField(max_length=100)
	subclass = models.CharField(max_length=100)
	role = models.CharField(max_length=50)
	admin = models.CharField(max_length=50)
	timestamp = models.DateTimeField()

	def __unicode__(self):
		return self.url

class DTAdmin(admin.ModelAdmin):
      list_display = ('name','timestamp')


admin.site.register(ServiceDT,DTAdmin)