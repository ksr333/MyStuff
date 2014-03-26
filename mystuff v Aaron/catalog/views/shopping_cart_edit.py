from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, logout, login
from . import templater
from account import models as amod
from manager import models as mmod


def process_request(request):
    if request.urlparams[2] == 'delete':
        cart = request.session.get('cart', {})
        pid = request.urlparams[0]
        if pid in cart:
            del cart[pid]

        request.session['cart'] = cart

        return HttpResponseRedirect('/catalog/shopping_cart/')

    ## elif request.urlparams[2] == 'update':
    ##     cart = request.session.get('cart', {})
    ##     quantity = int(request.urlparams[1])
    ##     pid = request.urlparams[0]
    ##     cart[pid] = quantity
    ##     request.session['cart'] = cart
    ##
    ##     return HttpResponseRedirect('/catalog/shopping_cart')

    else:
        catalog = mmod.ProductSpecification.objects.get(id=request.urlparams[0])
        quantity = int(request.urlparams[1])
        cart = request.session.get('cart', {})
        pid = str(catalog.id)

        if pid in cart:
            cart[pid] += quantity
        else:
            cart[pid] = quantity
        request.session['cart'] = cart

        return HttpResponseRedirect('/catalog/products/')