from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, AddProductForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product, CustomUser, Cart, CartItem, Order, OrderItem
from django.db import IntegrityError
from django.http import JsonResponse


def home(request):
    return redirect("dashboard")

class Regsiter(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password"]

            try:
                CustomUser.objects.create_user(
                    username=username, 
                    email=email,
                    phone_number=phone_number,
                    password=password
                )
                return redirect("dashboard")
            except IntegrityError:
                messages.error(request, "Username, email, or phone number already exists!")
                return render(request, "register.html", {"form": form})

        return render(request, "register.html", {"form": form})    
    
class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    
        return render(request, "login.html", {"form": form})   

class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out!")
        return redirect("login")
    
class UserDetail(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        return render(request, "user_detail.html", {"user":request.user})    

class Dashboard(View):
    def get(self, request):
        query = request.GET.get("q")

        if query:
            products = Product.objects.filter(name__icontains=query)
        else:
            products = Product.objects.all()

        return render(request, "home.html", {
            "products": products
        })
    
class AddProduct(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = "login"  # Redirect if not logged in

    def test_func(self):
        return self.request.user.is_staff  # Only staff users allowed

    def handle_no_permission(self):
        messages.error(self.request, "You are not authorized to add products")
        return redirect("dashboard")

    def get(self, request):
        form = AddProductForm()
        return render(request, "add_product.html", {"form": form})

    def post(self, request):
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, f"{product.name} added successfully!")
            return redirect("dashboard")
        return render(request, "add_product.html", {"form": form})
    
class UpdateProduct(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        messages.error(self.request, "You are not authorized to update products")
        return redirect("dashboard")

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = AddProductForm(instance=product)
        return render(request, "edit_product.html", {"form": form, "product": product})
    
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"{product.name} updated successfully!")
            return redirect("dashboard")
        
        messages.error(request, "Please correct the errors below.")
        return render(request, "edit_product.html", {"form": form, "product": product})

class DeleteProduct(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, "You are not authorized to delete products")
        return redirect("dashboard")

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, "delete_product_confirm.html", {"product": product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        messages.success(request, f"{product.name} has been deleted successfully!")
        return redirect("dashboard")

class AddToCart(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, 
            product=product
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        # Check if AJAX request
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({
                "success": True,
                "product_name": product.name,
                "quantity": cart_item.quantity
            })

        # Fallback for normal POST
        return redirect("dashboard")
    
class ViewCart(LoginRequiredMixin, View):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        
        products = 0
        total = 0
            
        for cart_item in cart_items:
                total += cart_item.product.price * cart_item.quantity
                products +=1

        context = {
                "cart": cart,
                "items": products,
                "total_price": total,
            }

        return render(request, "cart.html", context)

class ViewCartItems(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        for cart in cart_items:
            total_price = cart.product.price * cart.quantity
             
            cart.price = total_price
            cart.save()
        return render(request, "cart_items.html", {"cart_items": cart_items})

class UpdateCart(LoginRequiredMixin, View):
    
    def get(self, request):
        cart = Cart.objects.get(user=request.user)
        cart_list = CartItem.objects.filter(cart=cart)
        return render(request, "update_cart.html", {"cart_list": cart_list})
    
    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        action = request.POST.get("action")

        if action and action.startswith("remove_"):
            item_id = action.split("_")[1]
            CartItem.objects.filter(id=item_id, cart=cart).delete()
            return redirect("update_cart")
        
        if action == "save":
            for item in cart_items:
                qty = request.POST.get(f"quantity_{item.id}")

                if qty:
                    item.quantity = int(qty)
                    item.save()
            return redirect("view_cart")

        return redirect("update_cart")

class DeleteCart(LoginRequiredMixin, View):

    def get(self, request):
        cart = Cart.objects.filter(user=request.user).first()

        if not cart:
            messages.info(request, "Your cart is already empty.")
            return redirect("dashboard")

        return render(request, "delete_cart_confirm.html", {"cart": cart})

    def post(self, request):
        cart = Cart.objects.filter(user=request.user).first()

        if cart:
            cart.delete()
            messages.success(request, "Your cart has been cleared successfully.")

        return redirect("dashboard")

class CreateOrder(LoginRequiredMixin, View):
    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        if not cart_items.exists():
            return redirect("view_cart")

        order = Order.objects.create(
            user=request.user,
            total_price=0
        )

        total = 0
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.price
            )
            total += item.price
            item.product.stock_quantity-=item.quantity
            item.product.save()

        order.total_price = total
        order.save()

        return redirect("order_list")
    
class ViewOrders(LoginRequiredMixin, View):
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        return render(request, "order_list.html", {"orders": orders})

class ViewOrderItems(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id, user=request.user)
        order_items = OrderItem.objects.filter(order=order)
        return render(request, "order_items.html", {"order_items": order_items, "order": order})

class CancelOrder(LoginRequiredMixin, View):
    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id, user=request.user)
        return render(request, "cancel_order_confirm.html", {"order": order})

class ConfirmCancelOrder(LoginRequiredMixin, View):
    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id, user=request.user)
        action = request.POST.get("action")

        if action == "confirm":
            order.delete()
            messages.success(request, f"Order #{order.id} has been canceled successfully.")
        else:
            messages.info(request, f"Order #{order.id} was not canceled.")
        
        return redirect("order_list")


