from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, logout, login
from . import templater
from account import models as amod
from manager import models as mmod


def process_request(request):
    categoryID = request.urlparams[0]
    category_param = {}
    if categoryID is not '':
        ##['key'] = value
        category_param['category'] = categoryID
    else:
        category_param = {}

    product = mmod.Product_Specification.objects.filter(**category_param).exclude(active=False)

    template_vars = {
        'products_detail_key': product,
    }

    return templater.render_to_response(request, 'products_detail.html', template_vars)