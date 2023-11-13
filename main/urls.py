from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ProjectView, WorkHistoryView, BlogView, ContactView)


router = DefaultRouter()
router.register('project-url', ProjectView, basename='project-url')
router.register('work-history-url', WorkHistoryView, basename='work-history-url')
router.register('blog-url', BlogView, basename='blog-url')
router.register('contact-url', ContactView, basename='contact-url')

urlpatterns = [
	path('', include(router.urls)),
]
