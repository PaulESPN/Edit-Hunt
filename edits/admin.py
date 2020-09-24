from django.contrib import admin
from .models import Edit, Vote
from embed_video.admin import AdminVideoMixin

admin.site.register(Edit)
admin.site.register(Vote)
# Register your models here.
