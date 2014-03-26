# from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from calculator.models import *
from manager import models as mmod
from . import templater
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
    if request.user.is_customer:
        return HttpResponseRedirect("/homepage/")
    ##categoryID = request.urlparams[0]
    ##category_param = {}
    ##if categoryID is not '':
    ##       category_param['category'] = categoryID
    ## else:
    ##         category_param = {}

    nsp = mmod.NonSerializedProduct.objects.exclude(is_active=False).order_by('name')
    template_vars = {
        'non_serialized_product_key': nsp,
    }

    return templater.render_to_response(request, 'non_serialized_product_list.html', template_vars)

    return HttpResonseRedirect('non_serialized_product_view')

