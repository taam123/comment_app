from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
import uuid


class Comment(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey("auth.User", null=True, blank=True)
	url = models.URLField()
	content = models.TextField()
	allow_annon = models.BooleanField(default=True)
	timestamp = models.DateTimeField(blank=True)
	updated = models.DateTimeField(blank=True)


	def __unicode__(self):
		return self.url

	def save(self, *args, **kwargs):
		import pdb;pdb.set_trace();
		if self._state.adding == True:
			self.timestamp = timezone.now()
		self.updated = timezone.now()
		return super(Comment, self).save(*args, **kwargs)