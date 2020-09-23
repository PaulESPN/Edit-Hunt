from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Edit
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request, 'edits/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon']:
            edit = Edit()
            edit.title = request.POST['title']
            edit.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                edit.url = request.POST['url']
            else:
                edit.url = 'https://' + request.POST['url']
            edit.icon = request.FILES['icon']
            edit.pub_date = timezone.datetime.now()
            edit.hunter = request.user
            edit.save()
            return redirect('home')

        else:
            return render(request, 'edits/create.html',{'error':'All fields must be filled out'})
    else:
        return render(request, 'edits/create.html')
