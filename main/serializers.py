from rest_framework import serializers
from .models import (WorkHistoryModel, ProjectModel, BlogModel, ContactModel)


class WorkHistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = WorkHistoryModel
		fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProjectModel
		fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = BlogModel
		fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContactModel
		fields = '__all__'
