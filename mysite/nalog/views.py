from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm, ContactForm
from .models import UserResults
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

def index(request):
    if request.POST.get('num') != 0 and request.method == 'POST':
        numberNew = request.POST.get('number')
        if str(request.POST.get('countChild')):
            countChildNew = str(request.POST.get('countChild'))
        else:
            countChildNew = '0'
        per13divNew = str(request.POST.get('per13div'))
        per13New = str(request.POST.get('per13'))
        per30New = str(request.POST.get('per30'))
        checkChildNew = str(request.POST.get('checkChild'))
        checkInvNew = str(request.POST.get('checkInv'))
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

        if user_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['password_confirmation']:
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        elif user_form.data['password'] != user_form.data['password_confirmation']:
            user_form.add_error('password_confirmation', 'The passwords do not match')
        else:
            print(user_form.errors)
            print(profile_form.errors)
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
            messages.warning(request, 'Invalid login details')
            return render(request, 'nalog/login.html')
    else:
        return render(request, 'nalog/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def office(request):
    user = request.user
    users_list = UserResults.objects.filter(IDuser=user).order_by('-dateStart')
    context_dict = {'users_list': users_list}
    return render(request, 'nalog/office.html', context_dict)

def calculate(request):
    users_list = UserResults.objects.order_by('-dateStart')
    context_dict = {'users_list': users_list}
    return render(request, 'nalog/calc.html', context_dict)

def feedback(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			copy = form.cleaned_data['copy']

			recipients = ['zelenova.yulia@mail.ru']
			#Если пользователь захотел получить копию себе, добавляем его в список получателей
			if copy:
				recipients.append(sender)
			try:
				send_mail(subject, message, 'zelenova.yulia@mail.ru', recipients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'nalog/index.html')
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'nalog/feedback.html', {'form': form})