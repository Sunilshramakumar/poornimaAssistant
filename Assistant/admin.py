from calendar import Calendar
from multiprocessing import Event
from django.contrib import admin
from .models import Notice, Profile, Event, calendardetails
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'designation', 'specialization', 'achivements')

@admin.register(Event)
class EventForm(admin.ModelAdmin):
    list_display = ('id', 'ename', 'eorganizers', 'ediscription', 'ecoordinators')

@admin.register(Notice)
class NoticeForm(admin.ModelAdmin):
    list_display = ('id','date', 'notice')

@admin.register(calendardetails)
class CalenderForm(admin.ModelAdmin):
    list_display = ('id', 'month', 'date', 'purpose')

