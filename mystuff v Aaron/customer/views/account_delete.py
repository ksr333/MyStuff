from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . import templater
from account import models as amod
from django.contrib.auth import logout


def process_request(request):

    user = request.user
    logout(request)
    user.is_active = False
    user.save()

    return HttpResponseRedirect('/homepage/index')



