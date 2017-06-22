from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm
from .models import UserResults
from django.utils import timezone

def index(request):
    if request.POST.get('num') != 0 and request.method == 'POST':
        numberNew = request.POST.get('number')
        countChildNew = str(request.POST.get('countChild'))
        per13divNew = bool(request.POST.get('per13div'))
        per13New = bool(request.POST.get('per13'))
        per30New = bool(request.POST.get('per30'))
        checkChildNew = bool(request.POST.get('checkChild'))
        checkInvNew = bool(request.POST.get('checkInv'))
        startDateNew = timezone.now()
        user = request.user
        new = UserResults(IDuser=user, number=numberNew, countChild=countChildNew, per13div=per13divNew,
                        per13=per13New, per30=per30New, checkChild=checkChildNew, checkInv=checkInvNew, dateStart=startDateNew)
        new.save()
    context = {'boldmessage': 'lmao'}
    return render(request, 'nalog/index.html', context=context)
    
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm()

        if user_form.is_valid():
            user = user_form.save(commit=False)
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
    '''#users_list = UserResults.objects.order_by('-score')[:10]
    #users_list = UserResults.objects.filter(pk = IDuser).order_by('-dateStart')
    numberNew = request.POST.get('number')
    #UserResults.objects.update(number=numberNew)
    countChildNew = str(request.POST.get('countChild'))
    #UserResults.objects.update(countChild=countChildNew)
    per13divNew = bool(request.POST.get('per13div'))
    #UserResults.objects.update(per13div=per13divNew)
    per13New = bool(request.POST.get('per13'))
    #UserResults.objects.update(per13=per13New)
    per30New = bool(request.POST.get('per30'))
    #UserResults.objects.update(per30=per30New)
    checkChildNew = bool(request.POST.get('checkChild'))
    #UserResults.objects.update(checkChild=checkChildNew)
    checkInvNew = bool(request.POST.get('checkInv'))
    #UserResults.objects.update(checkInv=checkInvNew)
    user = request.user
    new = UserResults(IDuser=user, number=numberNew, countChild=countChildNew, per13div=per13divNew,
                        per13=per13New, per30=per30New, checkChild=checkChildNew, checkInv=checkInvNew)
    new.save()'''
    users_list = UserResults.objects.order_by('-dateStart')
    context_dict = {'users_list': users_list}
    return render(request, 'nalog/office.html', context_dict)

def calculate(request):
    users_list = UserResults.objects.order_by('-dateStart')
    context_dict = {'users_list': users_list}
    return render(request, 'nalog/calc.html', context_dict)