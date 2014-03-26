from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from calculator.models import *
from . import templater
from manager import models as mmod
from account import models as amod
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
    if request.user.is_customer:
        return HttpResponseRedirect("/homepage/")

    c = mmod.Category.objects.exclude(is_active=False).order_by('category_name')
    template_vars = {
        'category_key': c,
    }

    return templater.render_to_response(request, 'category_list.html', template_vars)

    return HttpResonseRedirect('/manager/category_add')

