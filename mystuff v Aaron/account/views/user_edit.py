from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . import templater
from account import models as amod
from django.contrib.auth.decorators import login_required

@login_required
def process_request (request):
    if request.user.is_customer:
        return  HttpResponseRedirect("/homepage")


def process_request(request):
  #Edit a store

    user = amod.User.objects.get(id=request.urlparams[0])

    form = User_Form(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'password': user.password,
        'email': user.email,
        'is_active': user.is_active,
        'is_superuser': user.is_superuser,
        'is_staff': user.is_staff,
        'is_customer': user.is_customer,

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
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.is_active = form.cleaned_data['is_active']
            user.is_superuser = form.cleaned_data['is_superuser']
            user.is_staff = form.cleaned_data['is_staff']
            user.is_customer = form.cleaned_data['is_customer']

            ##user.email = form.cleaned_data['email']
            ##user.street = form.cleaned_data['street']
            ##user.city = form.cleaned_data['city']
            ##user.state = form.cleaned_data['state']
            ##user.zipcode = form.cleaned_data['zipcode']
            ##user.country = form.cleaned_data['country']
            ##user.security_question = form.cleaned_data['security_question']
            ##user.security_answer = form.cleaned_data['security_answer']
            user.save()
            ##return HttpResponseRedirect('item_list_page')

    tvars = {
        'form': form,

    }
    return templater.render_to_response(request, 'user_edit.html', tvars)


class User_Form(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput())
    email = forms.CharField()
    is_active = forms.BooleanField(required=False)
    is_superuser = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    is_customer = forms.BooleanField(required=False)

    ##street = forms.CharField()
    ##city = forms.CharField()
    ##state = forms.CharField()
    ##zipcode = forms.CharField()
    ##country = forms.CharField()
    ##security_question = forms.CharField()
    ##security_answer = forms.CharField()


