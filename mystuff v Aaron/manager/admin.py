from django.db import models
from django.contrib import admin
from .models import *

# register any models here
admin.site.register(Store)
admin.site.register(StorePhone)
admin.site.register(Category)
##admin.site.register(Vendor)
admin.site.register(ProductSpecification)
admin.site.register(Transaction)
admin.site.register(JournalEntry)
admin.site.register(GeneralLedgerName)
admin.site.register(AccountTrans)
admin.site.register(RevenueSource)
admin.site.register(Coupon)
admin.site.register(Sale)
admin.site.register(SerializedProduct)
admin.site.register(NonSerializedProduct)
admin.site.register(RentalProduct)
admin.site.register(Service)
admin.site.register(DamageFee)
admin.site.register(Fee)
admin.site.register(Rental)
admin.site.register(LateFee)