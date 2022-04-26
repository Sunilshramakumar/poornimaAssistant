from attr import field
from Assistant.models import Notice, Profile, Event, calendardetails
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Profile
        fields = ['id', 'name', 'email', 'designation', 'specialization', 'achivements']

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'ename', 'eorganizers', 'ediscription', 'ecoordinators']

class NoticeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'date', 'notice']

class CalendarSerializers(serializers.ModelSerializer):
    class Meta:
        model = calendardetails
        fields = ['id', 'month', 'date', 'purpose']
