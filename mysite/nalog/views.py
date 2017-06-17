from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm
from .models import UserResults

def index(request):
    context = {'boldmessage': 'lmao'}
    return render(request, 'nalog/index.html', context=context)
    
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm()

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'nalog/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print('Invalid login details: {0}, {1}'.format(username, password))
            return HttpResponse('Invalid login details')
    else:
        return render(request, 'nalog/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def office(request):
    #users_list = UserResults.objects.order_by('-score')[:10]
    #users_list = UserResults.objects.filter(PrimaryKey = IDuser).order_by('-dateStart')
    users_list = UserResults.objects.order_by('-dateStart')
    context_dict = {'users_list': users_list}
    return render(request, 'nalog/office.html', context_dict)