from django.db import models
from django.contrib import admin
from .models import *

## register any models here

admin.site.register(SecurityQuestion)
admin.site.register(Session)
admin.site.register(User)
admin.site.register(Member)
admin.site.register(NewsletterInterestAreas)
admin.site.register(Employee)
admin.site.register(Commission)
admin.site.register(UserPhone)
admin.site.register(Address)
