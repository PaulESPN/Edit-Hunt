from django.shortcuts import render
from .models import Edit
# Create your views here.
def home(request):
    edits = Edit.objects
    return render(request, 'edits/home.html', {'edits':edits})
