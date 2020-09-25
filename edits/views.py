from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Edit, Vote
from django.utils import timezone
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    edits = Edit.objects.order_by('-votecounter')
    return render(request, 'edits/home.html', {'edits':edits})

@login_required(login_url='/accounts/signup')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['video']:
            edit = Edit()
            edit.title = request.POST['title']
            edit.video = request.POST['video']
            edit.pub_date = timezone.datetime.now()
            edit.hunter = request.user
            edit.save()
            return redirect('/edits/'+ str(edit.id))

        else:
            return render(request, 'edits/create.html',{'error':'All fields must be filled out'})
    else:
        return render(request, 'edits/create.html')

def detail(request, edit_id):
    edit = get_object_or_404(Edit, pk=edit_id)
    return render(request, 'edits/detail.html',{'edit':edit})

@login_required(login_url='/accounts/signup')
def upvote(request, edit_id):
    if request.method == 'POST':
        edit = get_object_or_404(Edit, pk=edit_id)
        if request.user != edit.hunter:
            try:
                Vote.objects.get(edit=edit, hunter=request.user)
            except:
                vote = Vote(edit=edit, hunter=request.user)
                vote.save()
                edit.votecounter += 1
                edit.save()
            else:
                votePass = Vote.objects.get(edit=edit, hunter=request.user)
                votePass.delete()
                edit.votecounter -= 1
                edit.save()


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        #return redirect('/edits/'+ str(edit.id))
