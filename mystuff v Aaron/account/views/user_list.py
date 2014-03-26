# from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account import models as amod
from . import templater
from django.contrib.auth.decorators import login_required

@login_required
def process_request (request):
    if request.user.is_customer:
        return  HttpResponseRedirect("/homepage")

def process_request(request):
    user = amod.User.objects.exclude(is_active=False).order_by('last_name')
    template_vars = {
        'userKey': user,
    }

    return templater.render_to_response(request, 'user_list.html', template_vars)

    return HttpResonseRedirect('/account/user_view')

