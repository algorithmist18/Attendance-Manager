from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Subject(models.Model):

	subject = models.CharField(max_length = 50)
	user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
	present = models.IntegerField(default = 0)
	absent = models.IntegerField(default = 0)
	cancel = models.IntegerField(default = 0)
	threshold = models.FloatField(default = 50.00)
	safe_bunks = models.IntegerField(default = 0)
	total = models.IntegerField(default = 0)
	#username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True)
	percent = models.FloatField(default = 0.00)
	notes = models.CharField(max_length = 140, default = '')
	#class Meta:

		#unique_together =  (("subject", "user"),)

