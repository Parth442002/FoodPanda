from django.contrib import admin
from .models import Item, OrderItem, Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'delivery_address',
                    ]
    list_display_links = [
        'user',
    ]
    list_filter = ['ordered',]
    search_fields = [
        'user__username',
    ]
admin.site.register(Order, OrderAdmin)
admin.site.register(Item)
admin.site.register(OrderItem)

