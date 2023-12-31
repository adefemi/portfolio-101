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

	def __str__(self):
		return f"{self.order} - {self.job_title} at {self.company_name}"


class ProjectModel(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	link = models.CharField(max_length=100)
	focused = models.BooleanField(default='false')
	order = models.IntegerField(unique=True)
	cover = models.ImageField(null=True, blank=True, upload_to='porfolio101')

	class Meta:
		ordering = ('order', )
	
	def __str__(self):
		return f"{self.order} - {self.name}"


class BlogModel(models.Model):
	title = models.CharField(unique=True, max_length=255)
	link = models.CharField(max_length=255)
	order = models.IntegerField(unique=True)
	cover = models.FileField(null=True, blank=True, upload_to='porfolio101')

	class Meta:
		ordering = ('order', )
		
	def __str__(self):
		return f"{self.order} - {self.title}"
	
class ContactModel(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} - {self.email}"
