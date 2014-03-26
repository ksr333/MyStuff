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

    rp = mmod.RentalProduct()

    form = Rental_Product_Form()

    if request.method == 'POST':
        form = Rental_Product_Form(request.POST)

        if form.is_valid():
            rp.name = form.cleaned_data['name']
            rp.serial_number = form.cleaned_data['serial_number']
            ##sp.category = form.cleaned_data['category']
            a = mmod.Category.objects.get(category_name=form.cleaned_data['category'])
            if a.is_active == True:
                rp.category = a
            else:
                rp.category
            ## v = mmod.Vendor.objects.get(name=form.cleaned_data['vendor'])
            ## if v.is_active:
            ##     v.vendor = v
            ## else:
            ##     v.vendor
            rp.description = form.cleaned_data['description']
            rp.purchase_price = form.cleaned_data['purchase_price']
            rp.sale_price = form.cleaned_data['sale_price']
            rp.on_back_order = form.cleaned_data['on_back_order']
            rp.currently_rented = form.cleaned_data['currently_rented']
            rp.transfer_history = form.cleaned_data['transfer_history']
            rp.damage_report = form.cleaned_data['damage_report']
            rp.rental_history = form.cleaned_data['rental_history']
            rp.item_condition = form.cleaned_data['item_condition']
            rp.rental_price = form.cleaned_data['rental_price']
            rp.item_status = form.cleaned_data['item_status']

            rp.discount = form.cleaned_data['discount']
            b = mmod.Store.objects.get(location_name=form.cleaned_data['store'])
            if b.is_active == True:
                rp.store = b
            else:
                rp.store
            rp.product_image = form.cleaned_data['product_image']
            rp.save()
            
            return HttpResponseRedirect('/manager/rental_product_list')

    tvars = {
        'form': form,

    }
    return templater.render_to_response(request, 'rental_product_add.html', tvars)


class Rental_Product_Form(forms.Form):
    name = forms.CharField()
    serial_number = forms.CharField()
    category = forms.ModelChoiceField(queryset=mmod.Category.objects.exclude(is_active=False), required="True")
    ##vendor = forms.ModelChoiceField(queryset=mmod.Vendor.objects.exclude(is_active=False), required=True)
    description = forms.CharField()
    purchase_price = forms.DecimalField()
    sale_price = forms.DecimalField()
    currently_rented = forms.BooleanField(required=False)
    on_back_order = forms.BooleanField(required=False)
    discount = forms.DecimalField()
    transfer_history = forms.CharField()
    store = forms.ModelChoiceField(queryset=mmod.Store.objects.exclude(is_active=False), required="True")
    product_image = forms.URLField(required=False)
    transfer_history = forms.CharField()
    damage_report = forms.CharField()
    rental_history = forms.CharField()
    item_condition = forms.CharField()
    rental_price = forms.CharField()
    item_status = forms.CharField()


    


