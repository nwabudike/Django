from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Room, Message


def home(request):
    return render(request, 'chat_apps/home.html')


def create_room(request):
    if request.method == 'POST':
        room = request.POST['room_name']
        username = request.POST['username']

        if Room.objects.filter(name=room).exists():
            return redirect('/' + room + '/?username=' + username)
        else:
            new_room = Room.objects.create(name=room)
            new_room.save()
            return redirect('/' + room + '/?username=' + username)


def chat_site(request, room):
    room_details = Room.objects.get(name=room)
    username = request.GET.get('username')
    return render(request, 'chat_apps/room.html', {
        'room_name': room,
        'username': username,
        'room_details': room_details,
    })


def send(request, room):
    messages = request.POST['messages']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=messages, user=username, room=room_id)
    new_message.save()
    return redirect('/'+room+'/?username='+username)


def getMessages(request,  room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})