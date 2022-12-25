from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token import *

from login_system import settings


def home(request):
    return render(request, 'info_app/home.html')


def signout(request):
    logout(request)
    messages.success(request, 'logged out successfully')
    return redirect('home')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, 'info_app/home.html', {'firstname': firstname})
        else:
            messages.error(request, 'user does not exist')
            return redirect('home')
    return render(request, 'info_app/signin.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        C_password = request.POST['C_password']

        if User.objects.filter(username=username):
            messages.error(request, 'Username already exist')
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, 'email already exist')
            return redirect('signup')
        if password != C_password:
            messages.error(request, 'The password does not match')
            return redirect('signup')
        if len(username) > 10:
            messages.error(request, 'User name must not b longer than 10')
            return redirect('signup')
        if not username.isalnum():
            messages.error(request, 'usename must contain only number or alphabet')
            return redirect('signup')

        create_user = User.objects.create_user(username, email, password)
        create_user.first_name = firstname
        create_user.last_name = lastname
        #create_user.Is_active = False
        create_user.save()
        messages.success(request, 'Accout created successfully')


        # for email functionality
        # subject = 'welcome to hillary app'
        # message = 'welcome' + create_user.first_name + '\n we would send a another email to activate your account'
        # from_list = settings.EMAIL_HOST_USER
        # to_list = [create_user.email]
        # send_mail(subject, message, from_list, to_list, fail_silently=True)
        #
        # current_site = get_current_site(request)
        # subject1 = 'Confirm your account '
        # message1 = render_to_string('email_confirmation.html', {
        #     'name': create_user.first_name,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(create_user.pk)),
        #     'token': token_generator.make_token(create_user)
        # })
        # from_list1 = settings.EMAIL_HOST_USER
        # to_list1 = [create_user.email]
        # send_mail(subject1, message1, from_list1, to_list1, fail_silently=True)

        return redirect('signin')

    return render(request, 'info_app/signup.html')

# for email functionality
# def activation(request, uid64, token):
#     try:
#         uid = force_bytes(urlsafe_base64_decode(uid64))
#         create_user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         create_user = None
#
#     if create_user is not None and token_generator.check_token(create_user, token):
#         create_user.is_active = True
#         create_user.save()
#         login(request, create_user)
#         return redirect('home')
#     else:
#         return render(request, 'activation_fail.html')
