from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . import templater
from django.contrib.auth import authenticate, login


def process_request(request):
    form = Login_Form()
    if request.method == "POST":
        form = Login_Form(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/homepage/index')
            else:
                pass
        else:
            pass
    tvars = {
        'form': form,
    }

    return templater.render_to_response(request, "login.html", tvars)


class Login_Form(forms.Form):
    username = forms.CharField(required=True, label="User Name")
    password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput())


def clean(self):
    user = authenticate(username=forms.cleaned_data['username'], password=forms.cleaned_data['password'])
    if user == None:
        raise forms.ValidationError("Incorrect Username and/or Password")
    return self.cleaned_data
