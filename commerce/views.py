from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, AddProductForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, CustomUser, Cart, CartItem, Order, OrderItem
from django.db import IntegrityError


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
    
class AddProduct(LoginRequiredMixin, View):
    def get(self, request):
        form = AddProductForm()
        return render(request, "add_product.html", {"form": form})

    def post(self, request):
        form = AddProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, f"{product.name} added successfully!")

            return redirect("dashboard")
        return render(request, "add_product.html", {"form": form})
    
class UpdateProduct(LoginRequiredMixin, View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk, user=request.user)
        form = AddProductForm(instance=product)
        return render(request, "edit_product.html", {"form": form, "product": product})
    
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk, user=request.user)
        form = AddProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"{product.name} updated successfully!")
            return redirect("dashboard")
        else:
            messages.error(request, "Please correct the errors below.")
        return render(request, "edit_product.html", {"form": form, "product": product})

class DeleteProduct(LoginRequiredMixin, View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk, user=request.user)
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

        return redirect("dashboard")
    
class ViewCart(LoginRequiredMixin, View):
    def get(self, request):
        carts = Cart.objects.filter(user=request.user)
        cart_list = CartItem.objects.filter(cart__in=carts)
        return render(request, "cart.html", {"cart_list": cart_list})









