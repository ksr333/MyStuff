from django.db import models
from account.models import User as User
from account.models import Commission as Commission
from account.models import Address as Address
from account.models import Member as Member
from account.models import Employee as Employee


class Store(models.Model):
    ##id
    is_active = models.BooleanField(default=True)
    manager = models.OneToOneField(User, related_name="Stores I Manage", blank=True, null=True)
    location_name = models.TextField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    zipcode = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.location_name


class StorePhone(models.Model):
    ##id
    store = models.ForeignKey(Store)
    is_active = models.BooleanField(default=True)
    phone_name = models.TextField(blank=True, null=True)
    phone_type = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    extension = models.IntegerField(blank=True, null=True)


class Category(models.Model):
    ##id
    is_active = models.BooleanField(default=True)
    category_name = models.TextField(blank=True, null=True)
    category_image = models.URLField()

    def __str__(self):
        return '%s' % self.category_name


## class Vendor(models.Model):
##     is_active = models.BooleanField(default=True)
##     name = models.TextField(blank=True, null=True)
##     street = models.TextField(blank=True, null=True)
##     city = models.TextField(blank=True, null=True)
##     state = models.TextField(blank=True, null=True)
##     zipcode = models.TextField(blank=True, null=True)
##     country = models.TextField(blank=True, null=True)
##     phone = models.IntegerField(blank=True, null=True)
##     contact = models.TextField(blank=True, null=True)

##     def __str__(self):
##         return '%s' % self.name

class ProductSpecification(models.Model):
    ##id
    category = models.ForeignKey(Category)
    ##vendor = models.ForeignKey(Vendor)
    is_active = models.BooleanField(default=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=50, decimal_places=2)
    sale_price = models.DecimalField(max_digits=50, decimal_places=2)
    brand_name = models.TextField(blank=True, null=True)
    on_back_order = models.BooleanField(default=False)
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    store = models.ForeignKey(Store, blank=True, null=True)
    product_image = models.URLField()


class Transaction(models.Model):
    ##id
    address = models.ForeignKey(Address)
    employee = models.ForeignKey(Employee)
    customer = models.ForeignKey(User)
    commission = models.ForeignKey(Commission)
    store = models.ForeignKey(Store)
    date = models.DateTimeField()
    subtotal = models.DecimalField(max_digits=50, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=50, decimal_places=2)
    payment_amount = models.DecimalField(max_digits=50, decimal_places=2)
    payment_type = models.DecimalField(max_digits=50, decimal_places=2)


class JournalEntry(models.Model):
    ##id
    date = models.DateTimeField()
    note = models.TextField(blank=True, null=True)


class GeneralLedgerName(models.Model):
    ##id
    ledger_name = models.TextField(blank=True, null=True)


class AccountTrans(models.Model):
    ##id
    journal_entry = models.ForeignKey(JournalEntry)
    general_ledger_name = models.ForeignKey(GeneralLedgerName)
    is_debit = models.BooleanField(default=True)


class RevenueSource(models.Model):
    ##id
    transaction = models.ForeignKey(Transaction)
    charge_amount = models.DecimalField(max_digits=50, decimal_places=2)


class Coupon(models.Model):
    ##id
    revenue_source = models.ForeignKey(RevenueSource)
    coupon_amount = models.DecimalField(max_digits=50, decimal_places=2)


class SerializedProduct(ProductSpecification):
    ##is_rental = models.BooleanField(default=False)
    serial_number = models.TextField(blank=True, null=True)
    transfer_history = models.TextField(blank=True, null=True)


class NonSerializedProduct(ProductSpecification):
    reorder_point = models.IntegerField(blank=True, null=True)
    max_level = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)


class RentalProduct(ProductSpecification):
    currently_rented = models.BooleanField(default=True)
    serial_number = models.TextField(blank=True, null=True)
    transfer_history = models.TextField(blank=True, null=True)
    damage_report = models.TextField(blank=True, null=True)
    rental_history = models.TextField(blank=True, null=True)
    item_condition = models.TextField(blank=True, null=True)
    rental_price = models.DecimalField(max_digits=50, decimal_places=2)
    item_status = models.TextField(blank=True, null=True)


class Sale(RevenueSource):
    quantity = models.IntegerField(blank=True, null=True)
    serialized_product = models.ForeignKey(SerializedProduct)
    non_serialized_product = models.ForeignKey(NonSerializedProduct)
    ##revenue_source = models.OneToOneField(RevenueSource, primary_key = True)


class Service(RevenueSource):
    service_amount = models.DecimalField(max_digits=50, decimal_places=2)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    note = models.TextField(blank=True, null=True)
    labor_hours = models.DecimalField(max_digits=50, decimal_places=2)


class Repair(Service):
    member = models.ForeignKey(Member)
    order_number = models.IntegerField(blank=True, null=True)
    item_name = models.TextField(blank=True, null=True)
    serial_number = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    problem_description = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    warranty = models.BooleanField(default=True)
    pick_up_date = models.DateTimeField()
    repair_damage_report = models.TextField(blank=True, null=True)


class DamageFee(models.Model):
    ##id
    damage_note = models.TextField(blank=True, null=True)
    damage_fee = models.DecimalField(max_digits=50, decimal_places=2)


class Rental(RevenueSource):
    member = models.ForeignKey(Member)
    date_rented = models.DateTimeField()
    date_due = models.DateTimeField()
    date_returned = models.DateTimeField()
    rental_damage_report = models.TextField(blank=True, null=True)
    rental_product = models.ForeignKey(RentalProduct)


class Fee(RevenueSource):
    rental = models.ForeignKey(Rental)
    is_waived = models.BooleanField(default=False)
    damage_fee = models.ForeignKey(DamageFee)


class LateFee(Fee):
    days_late = models.IntegerField(blank=True, null=True)
    late_fee = models.DecimalField(max_digits=50, decimal_places=2)
