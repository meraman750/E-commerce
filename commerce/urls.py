from django.urls import path
from .views import Regsiter, Login, Dashboard, Logout, UserDetail, AddProduct, UpdateProduct, DeleteProduct, AddToCart, ViewCart
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", Regsiter.as_view(), name="register"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"), 
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("profile/", UserDetail.as_view(), name="profile"),
    path("password/change/", auth_views.PasswordChangeView.as_view(
        template_name = "password_change.html",
        success_url = '/profile/'
    ), name="password_change"),
    path("add_product/", AddProduct.as_view(), name="add_product"),
    path("update/<int:pk>/", UpdateProduct.as_view(), name="update_product"),
    path("delete/<int:pk>/", DeleteProduct.as_view(), name="delete_product"),
    path("add-to-cart/<int:product_id>/", AddToCart.as_view(), name="add_to_cart"),
    path("cart/", ViewCart.as_view(), name="view_cart"),
]