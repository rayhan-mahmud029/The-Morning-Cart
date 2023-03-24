from django.contrib import admin
from django import template
# Register your models here.
from .models import Product
from .models import HomeBanner
from .models import Sale
from .models import Featured
register = template.Library()
admin.site.register(Product)
admin.site.register(HomeBanner)
admin.site.register(Sale)
admin.site.register(Featured)
