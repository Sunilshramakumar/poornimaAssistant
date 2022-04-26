from operator import ipow
from django.urls import path, include
from Assistant.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('assistant', views.UserViewSet, basename='user')
router.register('event', views.EventViewSet, basename='event')
router.register('notice', views.NoticeViewSet, basename='notice')
router.register('calendar', views.CalendarViewSet, basename='calendar')


urlpatterns = [
    path('', include(router.urls)),
    path('api_event/', include('rest_framework.urls', namespace='rest_framework')),
    path('api_notice/', include('rest_framework.urls', namespace='rest_framework')),
    path('api_calendar/', include('rest_framework.urls', namespace='rest_framework'))
]
