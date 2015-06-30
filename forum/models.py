from django.db import models
from time import time

# Create your models here.

#def get_upload_file_name(instance, filename):
#	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Query(models.Model):
	title = models.CharField(max_length=200)
	details = models.TextField()
	pub_date = models.DateTimeField('date published')
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)
	#thumbnail = models.FileField(upload_to=get_upload_file_name)
	def __str__(self):
		return self.title

class Comment(models.Model):
	name =  models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	query = models.ForeignKey(Query)
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0) 
