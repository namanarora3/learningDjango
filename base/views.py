from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.db.models  import Q
from .models import Room,Topic
from .forms import RoomForm
# Create your views here.
# rooms=[
#     {'id':1,'name':'Lets Learn python!'},
#     {'id':2,'name':'Lets Learn SQL!'},
#     {'id':3,'name':'Lets Learn Django!'},
# ]

def loginPage(request):
    if(request.user.is_authenticated):
        return redirect('home')
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist')
        
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        
    context={}
    return render(request,'base/login_registration.html',context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    room_count=rooms.count()
    context= {"rooms":rooms,'topics': Topic.objects.all(),'room_count':room_count}
    return render(request,'base/home.html',context)

def room(request,pk):
    i=Room.objects.get(id=pk)
    # for x in rooms:
    #     if x['id']==int(pk):
    #         i=x
    
    context={"room":i}
    return render(request,'base/room.html',context)

@login_required(login_url='login')
def room_form(request):
    form= RoomForm()
    if request.method == 'POST':    
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    context={'form': form}
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')   
def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    if(request.user == room.host):
        form=RoomForm(instance=room)
        if request.method == 'POST':
            form=RoomForm(request.POST,instance=room)
            if form.is_valid():
                form.save()
                return redirect(home)
        context={'form': form}
        return render(request,'base/room_form.html',context )
    else:
        return HttpResponse("you arent allowed here!!")

@login_required(login_url='login')
def deleteRoom(request,pk): 
    room=Room.objects.get(id=pk)
    if(request.user == room.host):
        if request.method == 'POST':
            room.delete()
            return redirect('home')
        return render(request,'base/delete.html',{'obj':room})
    else:
        return HttpResponse("you arent allowed here!!")