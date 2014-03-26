from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from . import templater
from account import models as amod


def process_request(request):
  #Edit an individual user information

    if request.urlparams[0] == 'delete':
        user = amod.User.objects.get(id=request.urlparams[0])
        user.is_active = False
        user.save()
        logout(request)
        return HttpResponseRedirect('/homepage/')

    user = amod.User.objects.get(id=request.urlparams[0])

    form = User_Form(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        ##'is_active': user.is_active,
        ##'is_superuser': user.is_superuser,
        ##'is_staff': user.is_staff,
        'username': user.username,
        'password': user.password,
        'email': user.email,
        ##'street': user.street,
        ##'city': user.city,
        ##'state': user.state,
        ##'zipcode': user.zipcode,
        ##'country': user.country,
        ##'security_question': user.security_question,
        ##'security_answer': user.security_answer,
    })

    if request.method == 'POST':
        form = User_Form(request.POST)

        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            ##user.is_active = form.cleaned_data['is_active']
            ##user.is_superuser = form.cleaned_data['is_superuser']
            ##user.is_staff = form.cleaned_data['is_staff']
            ##user.username = form.cleaned_data['username']
            ##user.password = form.cleaned_data['password']
            user.email = form.cleaned_data['email']
            ##user.street = form.cleaned_data['street']
            ##user.city = form.cleaned_data['city']
            ##user.state = form.cleaned_data['state']
            ##user.zipcode = form.cleaned_data['zipcode']
            ##user.country = form.cleaned_data['country']
            ##user.security_question = form.cleaned_data['security_question']
            ##user.security_answer = form.cleaned_data['security_answer']
            user.save()
            ##return HttpResponseRedirect('item_list_page')

    template_tvars = {
        'form': form,
    }
    return templater.render_to_response(request, 'account_edit.html', template_tvars)


class User_Form(forms.Form):
    ##is_active = forms.BooleanField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    ##is_superuser = forms.BooleanField(required=False)
    ##is_staff = forms.BooleanField(required=False)
    ##username = forms.CharField()
    ##password = forms.CharField()
    email = forms.CharField()
    ##street = forms.CharField()
    ##city = forms.CharField()
    ##state = forms.CharField()
    ##zipcode = forms.CharField()
    ##country = forms.CharField()
    ##security_question = forms.CharField()
    ##security_answer = forms.CharField()


