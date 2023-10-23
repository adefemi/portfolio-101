from django.contrib import admin
from .models import (WorkHistoryModel, ProjectModel, BlogModel)


admin.site.register(
	(WorkHistoryModel, ProjectModel, BlogModel)
)
