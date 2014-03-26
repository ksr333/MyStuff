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
  #Edit a category
    category = mmod.Category.objects.get(id=request.urlparams[0])
    form = CategoryForm(initial={
        'category_name': category.category_name,
    })

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category.category_name = form.cleaned_data['category_name']
            category.category_image = form.cleaned_data['category_image']
            category.save()
    tvars = {
        'form': form,
    }
    return templater.render_to_response(request, 'category_edit.html', tvars)


class CategoryForm(forms.Form):
    category_name = forms.CharField()
    category_image = forms.URLField(required=False)


