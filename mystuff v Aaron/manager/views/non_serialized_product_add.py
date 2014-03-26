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

    nsp = mmod.NonSerializedProduct()

    form = Non_Serialized_Product_Form()

    if request.method == 'POST':
        form = Non_Serialized_Product_Form(request.POST)

        if form.is_valid():
            nsp.name = form.cleaned_data['name']
            a = mmod.Category.objects.get(category_name=form.cleaned_data['category'])
            if a.is_active:
                nsp.category = a
            else:
                nsp.category
            ## v = mmod.Vendor.objects.get(name=form.cleaned_data['vendor'])
            ## if v.is_active:
            ##     v.vendor = v
            ## else:
            ##     v.vendor
            nsp.description = form.cleaned_data['description']
            nsp.purchase_price = form.cleaned_data['purchase_price']
            nsp.sale_price = form.cleaned_data['sale_price']
            nsp.reorder_point = form.cleaned_data['reorder_point']
            nsp.max_level = form.cleaned_data['max_level']
            nsp.quantity = form.cleaned_data['quantity']
            nsp.on_back_order = form.cleaned_data['on_back_order']
            nsp.discount = form.cleaned_data['discount']
            b = mmod.Store.objects.get(location_name=form.cleaned_data['store'])
            if b.is_active:
                nsp.store = b
            else:
                nsp.store
            nsp.product_image = form.cleaned_data['product_image']
            nsp.save()
            return HttpResponseRedirect('/manager/non_serialized_product_list')

    tvars = {
        'form': form,

    }
    return templater.render_to_response(request, 'non_serialized_product_add.html', tvars)


class Non_Serialized_Product_Form(forms.Form):
    name = forms.CharField()
    category = forms.ModelChoiceField(queryset=mmod.Category.objects.exclude(is_active=False), required="True")
    ##vendor = forms.ModelChoiceField(queryset=mmod.Vendor.objects.exclude(is_active=False), required=True)
    description = forms.CharField()
    purchase_price = forms.DecimalField()
    sale_price = forms.DecimalField()
    reorder_point = forms.IntegerField()
    max_level = forms.IntegerField()
    quantity = forms.IntegerField()
    on_back_order = forms.BooleanField(required=False)
    discount = forms.DecimalField()
    store = forms.ModelChoiceField(queryset=mmod.Store.objects.exclude(is_active=False), required="True")
    product_image = forms.URLField(required=False)




    


