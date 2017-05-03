from __future__ import unicode_literals

from django.db import models

class Auth(models.Model):
	p_user = models.IntegerField(default=0)
	p_pass = models.CharField(max_length=30)

	def __str__(self):
		return self.p_user

