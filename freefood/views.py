# Create your views here.

from django.http import JsonResponse
from freefood.models import Event, User
from datetime import datetime


def add_event(request):
    event = Event()
    event.Etitle = request.POST['Etitle']
    event.Etype = request.POST['Etype']
    year = request.POST['Eyear']
    month = request.POST['Emonth']
    day = request.POST['Eday']
    Estarthour = request.POST['Estarthour']
    Estartmin = request.POST['Estartmin']
    Eendhour = request.POST['Eendhour']
    Eendmin = request.POST['Eendmin']
    event.Estart = datetime(int(year), int(month), int(day), int(Estarthour), int(Estartmin))
    event.Eend = datetime(int(year), int(month), int(day), int(Eendhour), int(Eendmin))
    event.Eplace = request.POST['Eplace']
    event.Edescription = request.POST['Edescription']
    event.Eopen = request.POST['Eopen']
    event.Ersvps = request.POST['Ersvps']
    event.save()
    return JsonResponse({"status": 0})


def sign_up(request):
    user = User()
    user.username = request.POST['username']
    user.password = request.POST['password']
    user.location = request.POST['location']
    user.email = request.POST['email']
    user.tel = request.POST['tel']
    user.save()
    return JsonResponse({"status": 0})


def check_user_online(request):
    if 'username' in request.session:
        return JsonResponse({"status": 0,"username":request.session['username']})
    else:
        return JsonResponse({"status": 1})


def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = User.objects.get(username=username)
        if user:
            if password == user.password:
                request.session['username'] = username
                return JsonResponse({"status": 0})
            else:
                return JsonResponse({"status": 1, "msg": "wrong password or username"})
    except User.DoesNotExist:
        return JsonResponse({"status": 2, "msg": "user not exist!!"})


def show_events(request):
    # username = request.POST.get('username',0)
    events = Event.objects.all().values()
    res = []
    for i in range(len(events)):
        res.append(events[i])
    return JsonResponse({"status": 0,"data":res})


def show_event_user(request):
    username = request.POST.get('username',0)
    user = User.objects.get(username=username)
    events = user.EventsRegister.all().values_list('id', flat=True).values()
    res = []
    for i in range(len(events)):
        res.append(events[i])
    return JsonResponse({"status": 0,"data":res})


def add_event_user(request):
    username = request.POST['username']
    eventid = request.POST['eventId']
    user = User.objects.get(username=username)
    event = Event.objects.get(id=eventid)
    user.EventsRegister.add(event)
    return JsonResponse({"status": 0})


def remove_event_user(request):
    username = request.POST['username']
    eventid = request.POST['eventId']
    user = User.objects.get(username=username)
    event = Event.objects.get(id=eventid)
    user.EventsRegister.remove(event)
    return JsonResponse({"status": 0})
