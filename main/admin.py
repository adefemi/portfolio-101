from django.contrib import admin
from .models import (WorkHistoryModel, ProjectModel, BlogModel, ContactModel)


admin.site.register(
    (WorkHistoryModel, ProjectModel, BlogModel, ContactModel)
)
