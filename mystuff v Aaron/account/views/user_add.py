from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . import templater
from account import models as amod
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
    if request.user.is_customer:
        return HttpResponseRedirect("/homepage")


def process_request(request):
  #Edit a catalog_item
##    if request.user.isManager:
    user = amod.User()
    address = amod.Address()

    form = User_Form()

    if request.method == 'POST':
        form = User_Form(request.POST)

        if form.is_valid():
            
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            ##user.is_active = form.cleaned_data['is_active']
            ##user.is_superuser = form.cleaned_data['is_superuser']
            user.is_staff = form.cleaned_data['is_staff']
            user.is_customer = form.cleaned_data['is_customer']

            ## user.street = form.cleaned_data['street']

            ##user.city = form.cleaned_data['city']
            ##user.state = form.cleaned_data['state']
            ##user.zipcode = form.cleaned_data['zipcode']
            ##user.country = form.cleaned_data['country']
            ##user.security_question = form.cleaned_data['security_question']
            ##user.security_answer = form.cleaned_data['security_answer']

            user.save()
            
            return HttpResponseRedirect('/account/user_list')

    tvars = {
        'form': form,

    }
    return templater.render_to_response(request, 'user_add.html', tvars)
##else:
##    redirect to here

class User_Form(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    ##is_active = forms.BooleanField()
    ##is_superuser = forms.BooleanField(required=False)
    username = forms.CharField()
    password = forms.CharField()
    is_staff = forms.BooleanField(required=False)
    is_customer = forms.BooleanField(required=False)
    ##street = forms.CharField()
    ##city = forms.CharField()
    ##state = forms.CharField()
    ##zipcode = forms.IntegerField()
    ##country = forms.CharField()
    ##security_question = forms.CharField()
    ##security_answer = forms.CharField()


