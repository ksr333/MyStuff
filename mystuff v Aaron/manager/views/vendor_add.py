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

    v = mmod.Vendor()

    form = Vendor_Form()

    if request.method == 'POST':
        form = Vendor_Form(request.POST)

        if form.is_valid():
            v.name = form.cleaned_data['name']
            v.street = form.cleaned_data['street']
            v.city = form.cleaned_data['city']
            v.state = form.cleaned_data['state']
            v.zipcode = form.cleaned_data['zipcode']
            v.country = form.cleaned_data['country']
            v.phone = form.cleaned_data['phone']
            v.contact = form.cleaned_data['contact']
            v.save()
            
            return HttpResponseRedirect('/manager/vendor_list')

    tvars = {
        'form': form,

    }
    return templater.render_to_response(request, 'vendor_add.html', tvars)


class Vendor_Form(forms.Form):
    name = forms.CharField()
    street = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zipcode = forms.CharField()
    country = forms.CharField()
    phone = forms.CharField()
    contact = forms.CharField()


    


