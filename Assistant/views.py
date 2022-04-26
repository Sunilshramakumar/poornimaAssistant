import email
from multiprocessing import Event
from ssl import Purpose
from unicodedata import name
from django.shortcuts import render,HttpResponseRedirect
from Assistant.models import Profile
from .forms import EventForm, SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import ProfileDetails
from .models import Profile
from .forms import EventForm
from .models import Event
from .forms import NoticeForm
from .models import Notice
from .forms import CalendarForm
from .models import calendardetails
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required



# Home
def home(request):
    return render(request, 'Assistant/home.html')
# About
def about(request):
    return render(request, 'Assistant/about.html')


# DashBoard
def dashboard(request):
    return render(request, 'Assistant/dashboard.html')

def news(request):
    return render(request, 'Assistant/news.html')

def notice(request):
    if request.method == 'POST':
        nm = NoticeForm(request.POST)
        if nm.is_valid():
            dt = nm.cleaned_data['date']
            nm = nm.cleaned_data['notice']
            
            reg = Notice(date = dt,notice = nm)
            reg.save()
            nm = NoticeForm()
    else:
        nm = NoticeForm()
    note = Notice.objects.all()
    return render(request, 'Assistant/notice.html', {'form' : nm, 'ntu' : note})

def notice_update(request, id):
    if request.method == 'POST':
        pi = Notice.objects.get(pk=id)
        fm = NoticeForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = Notice.objects.get(pk=id)
        fm = NoticeForm(instance=pi)
    return render(request, 'Assistant/noticeupdate.html', {'form' : fm})

def notice_delete(request,id):
    if request.method == 'POST':
        pi = Notice.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/notice/')
        

def calendar_data(request):
    if request.method == 'POST':
        nm = CalendarForm(request.POST)
        if nm.is_valid():
            mo = nm.cleaned_data['month']
            da = nm.cleaned_data['date']
            pu = nm.cleaned_data['purpose']
            reg = calendardetails(month = mo, date = da, purpose = pu)
            reg.save()
            nm = CalendarForm()
    else:
        nm = CalendarForm()
    note = calendardetails.objects.all()
    return render(request, 'Assistant/calender.html', {'form' : nm, 'ntu' : note})

def calender_update_data(request,id):
    if request.method == 'POST':
        pi = calendardetails.objects.get(pk=id)
        fm = CalendarForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = calendardetails.objects.get(pk=id)
        fm = CalendarForm(instance=pi)
    return render(request, 'Assistant/calendarupdate.html', {'form' : fm})

#  pk = Primary key
# This function will delet

def calender_delete_data(request,id):
    if request.method == 'POST':
        pi = calendardetails.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/calender/')
        



def event_add_show(request):
    if request.method == 'POST':
        em = EventForm(request.POST)
        if em.is_valid():
            en = em.cleaned_data['ename']
            eo = em.cleaned_data['eorganizers']
            ed = em.cleaned_data['ediscription']
            ec = em.cleaned_data['ecoordinators']
            reg  = Event(ename = en, eorganizers = eo, ediscription = ed, ecoordinators = ec)
            reg.save()
            em = EventForm()
            # fm.save()
    else:
        em = EventForm()
    #  For show the whole data to user
    event = Event.objects.all() 
    return render(request, 'Assistant/event.html', {'form' : em, 'etu' : event})

def event_update_data(request,id):
    if request.method == 'POST':
        pi = Event.objects.get(pk=id)
        fm = EventForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = Event.objects.get(pk=id)
        fm = EventForm(instance=pi)
    return render(request, 'Assistant/eventupdate.html', {'form' : fm})

#  pk = Primary key
# This function will delet

def event_delete_data(request,id):
    if request.method == 'POST':
        pi = Event.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/event/')
        

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# DashBoard
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            # first_name = request.POST['first_name']
            # last_name = request.POST['last_name']
            email = request.POST['email']
            subject = 'Welcome to Poornima Assistant'
            message = f'Hi {username} we will help you to assistant.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            # messages.success(request, 'Congratulations you have successfully signed up !! Now you can Login!!')
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'Assistant/signup.html', {'form' : form})

# DashBoard
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upaas = form.cleaned_data['password']
                user = authenticate(username=uname, password=upaas)


                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully!!')
                    return HttpResponseRedirect('/home/')
        else:
            form = LoginForm()
        return render(request, 'Assistant/login.html', {'form' : form})
    else:
        return HttpResponseRedirect('/home/')
def user_profile(request):
    if request.method == "POST":
        fm = ProfileDetails(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            dg = fm.cleaned_data['designation']
            sp = fm.cleaned_data['specialization']
            ac = fm.cleaned_data['achivements']
            reg = Profile(name=nm, email=em, designation=dg, specialization=sp, achivements=ac)
            reg.save()
            fm = ProfileDetails()

    else:
        fm = ProfileDetails()
        stud = Profile.objects.all()
    return render(request, 'Assistant/profile.html', {'form' : fm})

def user_profile_update(request):
    
    stud = Profile.objects.all()
    return render(request, 'Assistant/updateprofile.html', {'stu' : stud})



def update_data(request,id):
    if request.method == 'POST':
        pi = Profile.objects.get(pk=id)
        fm = ProfileDetails(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = Profile.objects.get(pk=id)
        fm = ProfileDetails(instance=pi)
    return render(request, 'Assistant/profile.html', {'form' : fm})

def delete_data(request, id):
    if request.method == 'POST':
        pi = Profile.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/update/')

def department(request):
    return render(request, 'Assistant/department.html')

def facilities(request):
    return render(request, 'Assistant/facilities.html')
def studentcouncil(request):
    return render(request, 'Assistant/studentcouncil.html')



