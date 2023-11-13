from rest_framework.viewsets import ModelViewSet
from portfolio_101.utils import Helper
from .models import (WorkHistoryModel, ProjectModel, BlogModel, ContactModel)
from .serializers import (WorkHistorySerializer, ProjectSerializer, BlogSerializer, ContactSerializer)


class WorkHistoryView(ModelViewSet):
	queryset = WorkHistoryModel.objects.all()
	serializer_class = WorkHistorySerializer


class ProjectView(ModelViewSet):
	queryset = ProjectModel.objects.all()
	serializer_class = ProjectSerializer


class BlogView(ModelViewSet):
	queryset = BlogModel.objects.all()
	serializer_class = BlogSerializer


class ContactView(ModelViewSet):
	queryset = ContactModel.objects.all()
	serializer_class = ContactSerializer
