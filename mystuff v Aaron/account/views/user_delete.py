from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . import templater
from account import models as amod
from django.contrib.auth.decorators import login_required

@login_required
def process_request (request):
    if request.user.is_customer:
        return  HttpResponseRedirect("/homepage")


def process_request(request):
  ##Edit a store

    user = amod.User.objects.get(id=request.urlparams[0])

    if request.urlparams[1] == 'delete':

        user.is_active = False
        user.save()

    return HttpResponseRedirect('/account/user_list')



