from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . import templater
from manager import models as mmod
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
    if request.user.is_customer:
        return HttpResponseRedirect("/homepage/")
  ##Edit a store

    nsp = mmod.NonSerializedProduct.objects.get(id=request.urlparams[0])

    if request.urlparams[1] == 'delete':
        nsp.is_active = False
        nsp.save()

    return HttpResponseRedirect('/manager/non_serialized_product_list')



