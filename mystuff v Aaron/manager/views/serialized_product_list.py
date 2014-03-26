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
    sp = mmod.SerializedProduct.objects.exclude(is_active=False).order_by('name')
    template_vars = {
        'serialized_product_key': sp,
    }

    return templater.render_to_response(request, 'serialized_product_list.html', template_vars)

    return HttpResonseRedirect('/manager/serialized_product_add')
