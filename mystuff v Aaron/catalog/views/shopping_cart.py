from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, logout, login
from . import templater
from account import models as amod
from manager import models as mmod


def process_request(request):
    cart = request.session.get('cart', {})
    catalog = []
    amount = 0

    for c in cart:
        i = mmod.ProductSpecification.objects.get(id=str(c))
        catalog.append(i)

    for p in catalog:
        amount += p.sale_price * cart[str(p.id)]

    tvars = {
        'cart': cart,
        'catalog': catalog,
        'amount': amount,
    }

    return templater.render_to_response(request, 'shopping_cart.html', tvars)


