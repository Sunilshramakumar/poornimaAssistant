from cProfile import label
import email
from logging import PlaceHolder
from multiprocessing import Event
from multiprocessing.dummy import current_process
from pyexpat import model
from tkinter import Label
from attr import field, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from matplotlib import widgets
from django.utils.translation import gettext, gettext_lazy as _
from django.core import validators
from django import forms
from .models import Notice, Profile
from .models import Event
from .models import calendardetails

class ProfileDetails(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'email', 'designation', 'specialization', 'achivements']
        labels = {
            "name": "",
            "email": "",
            "designation" : "",
            "specialization" : "",
            "achivements" : "",
        }

        widgets = {

            'name' : forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control', 'style': 'font-family : times new roman;'}),
            'email' : forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'style': 'font-family : times new roman;'}),
            'designation' : forms.TextInput(attrs={'placeholder': 'Designation', 'class': 'form-control', 'style': 'font-family : times new roman; '}),
            'specialization' : forms.Textarea(attrs={'placeholder': 'Specialization', 'class': 'form-control', 'style': 'font-family : times new roman; height : 100px;'}),
            'achivements' : forms.Textarea(attrs={'placeholder': 'Achivements', 'class': 'form-control', 'style': 'font-family : times new roman; height : 100px;'}),
        }

class SignUpForm(UserCreationForm):
    # email = forms.EmailField(label= 'Email')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs= {'placeholder': 'Password','class' : 'form-control', 'style': 'font-family : times new roman; '}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs= {'placeholder': 'Confirm Password','class' : 'form-control', 'style': 'font-family : times new roman;'}))

    def clean_email(self):
        data = self.cleaned_data['email']
        if "@poornima.org" not in data:   # any check you need
            raise forms.ValidationError("Please Enter a Valid Domain of Your Organizatin!!")
        return data

    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
        "username" : "",
        "first_name" : "",
        "last_name" : "",
        "email" : ""
    }
        widgets = {'username' : forms.TextInput(attrs= {'placeHolder' : 'Username', 'class' : 'form-control', 'style': 'font-family : times new roman; '}),
        'first_name' : forms.TextInput(attrs= {'placeHolder' : 'First_Name', 'class' : 'form-control' , 'style': 'font-family : times new roman; margin-top : 15px;'}),
        'last_name' : forms.TextInput(attrs= {'placeHolder' : 'Last_Name', 'class' : 'form-control', 'style': 'font-family : times new roman; margin-top : 15px;'}),
        'email' : forms.EmailInput(attrs= {'placeHolder' : 'Email Address', 'class' : 'form-control', 'style': 'font-family : times new roman; margin-top : 15px;'})}


class LoginForm(AuthenticationForm):
    username =  UsernameField(widget=forms.TextInput(attrs={'autofocus' : True, 'class' : 'form-control', 'style' : 'width : 250px;' }))
    password = forms.CharField(label = _("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'class' : 'form-control' , 'style' : 'width : 250px;'})) 

    

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['ename', 'eorganizers', 'ediscription', 'ecoordinators']
        labels = {
            "ename": "",
            "eorganizers": "",
            "ediscription" : "",
            "ecoordinators" : "",
        }

        widgets = {
            'ename' : forms.TextInput(attrs={'placeholder': 'EventName', 'class': 'form-control', 'style': 'font-family : times new roman;'}),
            'eorganizers' : forms.TextInput(attrs={'placeholder': 'Organizers', 'class': 'form-control', 'style': 'font-family : times new roman;'}),
            'ediscription' : forms.Textarea(attrs={'placeholder': 'Discription', 'class': 'form-control', 'style': 'font-family : times new roman; height: 150px;'}),
            'ecoordinators' : forms.Textarea(attrs={'placeholder': 'Coordinators', 'class': 'form-control', 'style': 'font-family : times new roman; height : 100px;'})
        }

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['date','notice']
        labels = {"notice" : "","date" : "",}

        widgets = {
            'date' : forms.DateInput(attrs={'placeholder': 'Date', 'class': 'form-control', 'style': 'font-family : times new roman;'}),
            'notice' : forms.Textarea(attrs={'placeholder': 'Important News', 'class': 'form-control', 'style': 'font-family : times new roman; height : 250px;'})
        }

class CalendarForm(forms.ModelForm):
    class Meta:
        model = calendardetails
        fields = ['month','date','purpose']
        labels = {"month" : "",
                  "date" : "",
                  "purpose" : "",}

        widgets = {
            'month' : forms.TextInput(attrs={'placeholder': 'Month', 'class': 'form-control', 'style': 'font-family : times new roman;'}),
            'date' : forms.DateInput(attrs={'placeholder': 'Date', 'class': 'form-control', 'style': 'font-family : times new roman;'}),
            'purpose' : forms.Textarea(attrs={'placeholder': 'Purpose', 'class': 'form-control', 'style': 'font-family : times new roman;'})
        }


        