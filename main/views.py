from rest_framework.viewsets import ModelViewSet
from portfolio_101.utils import Helper
from .models import (WorkHistoryModel, ProjectModel, BlogModel)
from .serializers import (WorkHistorySerializer, ProjectSerializer, BlogSerializer)


class WorkHistoryView(ModelViewSet):
	queryset = WorkHistoryModel.objects.all()
	serializer_class = WorkHistorySerializer


class ProjectView(ModelViewSet):
	queryset = ProjectModel.objects.all()
	serializer_class = ProjectSerializer


class BlogView(ModelViewSet):
	queryset = BlogModel.objects.all()
	serializer_class = BlogSerializer
