from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.
# ##################### step 5 ####################################
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

# ##################### step 6 ####################################
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')

# #################### STEP 5.1
# add CartAdmin
admin.site.register(Cart, CartAdmin)

# #################### STEP 6.1
# add CartItemAdmin
admin.site.register(CartItem, CartItemAdmin)

