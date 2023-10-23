from django.db import models


class WorkHistoryModel(models.Model):
	job_title = models.CharField(max_length=100)
	company_name = models.CharField(max_length=100)
	start_date = models.CharField(max_length=20)
	end_date = models.CharField(max_length=20)
	description = models.TextField()
	order = models.IntegerField(unique=True)
	logo = models.ImageField(null=True, blank=True, upload_to='porfolio101')

	class Meta:
		ordering = ('order', )


class ProjectModel(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	link = models.CharField(max_length=100)
	focused = models.BooleanField(default='false')
	order = models.IntegerField(unique=True)
	cover = models.ImageField(null=True, blank=True, upload_to='porfolio101')

	class Meta:
		ordering = ('order', )


class BlogModel(models.Model):
	title = models.CharField(unique=True, max_length=255)
	link = models.CharField(max_length=255)
	order = models.IntegerField(unique=True)
	cover = models.FileField(null=True, blank=True, upload_to='porfolio101')

	class Meta:
		ordering = ('order', )
