from multiprocessing import Event
from django.http import QueryDict
from yaml import serialize_all
from Assistant.models import Notice, Profile, calendardetails
from Assistant.models import Event
from Assistant.api.serializers import CalendarSerializers, UserSerializers , EventSerializers, NoticeSerializers
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset =  Profile.objects.all()
    serializer_class = UserSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class CalendarViewSet(viewsets.ModelViewSet):
    queryset = calendardetails.objects.all()
    serializer_class = CalendarSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

