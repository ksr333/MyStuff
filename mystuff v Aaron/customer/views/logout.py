from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . import templater
from django.contrib.auth import logout


def process_request(request):
        logout(request)
        return HttpResponseRedirect("/homepage/index")

