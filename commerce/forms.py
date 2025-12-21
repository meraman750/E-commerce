from django import forms
from .models import Product
from phonenumber_field.formfields import PhoneNumberField

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone_number = PhoneNumberField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class AddProductForm(forms.ModelForm):
    price = forms.DecimalField(min_value=0.01, max_digits=10, decimal_places=2)
    stock_quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = Product
        fields = ["name", "description", "image", "price", "category", "stock_quantity"]
