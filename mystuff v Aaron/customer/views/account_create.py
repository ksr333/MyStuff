from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, logout, login
from . import templater
from account import models as amod


def process_request(request):
  #Edit a catalog_item
##    if request.user.isManager:
    user = amod.User()

    form = User_Form()

    if request.method == 'POST':
        form = User_Form(request.POST)

        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            ##user.street = form.cleaned_data['street']

            ##user.city = form.cleaned_data['city']
            ##user.state = form.cleaned_data['state']
            ##user.zipcode = form.cleaned_data['zipcode']
            ##user.country = form.cleaned_data['country']
            user.is_customer = True
            user.is_staff = False
            user.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password'])

            login(request, user)

            return HttpResponseRedirect('/homepage')

    tvars = {
        'form': form,

    }
    return templater.render_to_response(request, 'account_create.html', tvars)


class User_Form(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()

    ##street = forms.CharField()
    ##city = forms.CharField()
    ##state = forms.CharField()
    ##zipcode = forms.IntegerField()
    ##country = forms.CharField()
    ##is_active = forms.BooleanField()
    ##is_superuser = forms.BooleanField(required=False)
    ##is_staff = forms.BooleanField(required=False)
    ##security_question = forms.CharField()
    ##security_answer = forms.CharField()


