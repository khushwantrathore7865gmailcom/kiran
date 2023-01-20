from django.contrib import admin
from .models import Categories, Product, Clients, Order, OrderHistory, Contact

admin.site.register(Product)
admin.site.register(Clients)
admin.site.register(Categories)
admin.site.register(Order)
admin.site.register(OrderHistory)
admin.site.register(Contact)
