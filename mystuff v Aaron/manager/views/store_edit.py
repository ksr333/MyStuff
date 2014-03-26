from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . import templater
from manager import models as mmod
from account import models as amod
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
    if request.user.is_customer:
        return HttpResponseRedirect("/homepage/")
  #Edit a store

    store = mmod.Store.objects.get(id=request.urlparams[0])

    form = StoreForm(initial={
        'location_name': store.location_name,

        'street': store.street,
        'city': store.city,
        'state': store.state,
        'zipcode': store.zipcode,
        'country': store.country,
        })

    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store.location_name = form.cleaned_data['location_name']
            a = amod.User.objects.get(username=form.cleaned_data['manager'])
            if a.is_staff == True:
                store.manager = a
            else:
                store.manager
            store.street = form.cleaned_data['street']
            store.city = form.cleaned_data['city']
            store.state = form.cleaned_data['state']
            store.zipcode = form.cleaned_data['zipcode']
            store.country = form.cleaned_data['country']
            store.save()

    tvars = {
        'form': form,

    }
    return templater.render_to_response(request, 'store_edit.html', tvars)


class StoreForm(forms.Form):
    location_name = forms.CharField()
    manager = forms.ModelChoiceField(queryset=amod.User.objects.exclude(is_staff=False), required="False")
    street = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zipcode = forms.IntegerField()
    country = forms.CharField() 

