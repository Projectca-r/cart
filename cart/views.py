from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View

from .models import *
from .forms import *
# Create your views here.

def carts_list(request):
    carts = Cart.objects.first()
    context = {
        'carts': carts,
    }
    return render(request, 'cart/cart_list.html', context=context)

class CartCreate(View):
    def get(self, request):
        form = CartForm
        context = {
            'form': form,
        }
        return render(request, 'cart/cart_create.html', context=context)



# def cart_create(request, slug):
#     product = {
#         Product_TV,
#         Product_Phone,
#         Product_a_laptop,
#     }.objects.get(slug=slug)
#     new_item = CartItem.objects.Create(product=product)
#     cart = Cart.objects.first()
#     if new_item not in cart.items.all():
#         cart.items.add(new_item)
#         cart.save()
#         return redirect('/cart/')