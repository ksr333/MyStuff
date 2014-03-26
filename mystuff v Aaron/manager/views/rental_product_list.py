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
    rp = mmod.RentalProduct.objects.exclude(is_active=False).order_by('name')
    template_vars = {
        'rental_product_key': rp,
    }

    return templater.render_to_response(request, 'rental_product_list.html', template_vars)

    return HttpResonseRedirect('/manager/serialized_product_add')
