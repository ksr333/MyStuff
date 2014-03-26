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
  #Edit a store

    sp = mmod.SerializedProduct.objects.get(id=request.urlparams[0])

    form = SerializedProduct_Form(initial={
        'name': sp.name,
        'serial_number': sp.serial_number,
        'description': sp.description,
        'category': sp.category,
        'purchase_price': sp.purchase_price,
        'sale_price': sp.sale_price,
        'on_back_order': sp.on_back_order,
        'discount': sp.discount,
        'transfer_history': sp.transfer_history,
        'product_image': sp.product_image,
        ##'vendor': sp.vendor,
    })

    if request.method == 'POST':
        form = SerializedProduct_Form(request.POST)

        if form.is_valid():
            sp.name = form.cleaned_data['name']
            sp.serial_number = form.cleaned_data['serial_number']
            sp.description = form.cleaned_data['description']
            ##nsp.category = form.cleaned_data['category']
            a = mmod.Category.objects.get(category_name=form.cleaned_data['category'])
            if a.is_active == True:
                sp.category = a
            else:
                sp.category
            ## v = mmod.Vendor.objects.get(name=form.cleaned_data['vendor'])
            ## if v.is_active:
            ##     v.vendor = v
            ## else:
            ##     v.vendor
            sp.purchase_price = form.cleaned_data['purchase_price']
            sp.sale_price = form.cleaned_data['sale_price']
            sp.on_back_order = form.cleaned_data['on_back_order']
            sp.discount = form.cleaned_data['discount']
            sp.transfer_history = form.cleaned_data['transfer_history']
            b = mmod.Store.objects.get(location_name=form.cleaned_data['store'])
            if b.is_active == True:
                sp.store = b
            else:
                sp.store
            sp.product_image = form.cleaned_data['product_image']
            ##sp.is_rental = form.cleaned_data['is_rental']
            sp.save()
            ##return HttpResponseRedirect('list_page')

    tvars = {
        'form': form,

    }
    return templater.render_to_response(request, 'serialized_product_edit.html', tvars)


class SerializedProduct_Form(forms.Form):
    name = forms.CharField()
    serial_number = forms.CharField()
    description = forms.CharField()
    name = forms.CharField()
    category = forms.ModelChoiceField(queryset=mmod.Category.objects.exclude(is_active=False), required="True")
    purchase_price = forms.DecimalField()
    sale_price = forms.DecimalField()
    on_back_order = forms.BooleanField(required=False)
    discount = forms.DecimalField()
    transfer_history = forms.CharField()
    store = forms.ModelChoiceField(queryset=mmod.Store.objects.exclude(is_active=False), required="True")
    product_image = forms.URLField(required=False)
    ##is_rental = forms.BooleanField(required=False)
    

