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
    v = mmod.Vendor.objects.exclude(is_active=False).order_by('name')
    template_vars = {
        'vendor_key': v,
    }

    return templater.render_to_response(request, 'vendor_list.html', template_vars)

    return HttpResonseRedirect('/manager/serialized_product_add')
