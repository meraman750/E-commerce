from django.urls import path
from .views import ( Regsiter, Login, home,
Dashboard, Logout, UserDetail, 
AddProduct, UpdateProduct, DeleteProduct, 
AddToCart, ViewCart, UpdateCart, 
ViewCartItems, DeleteCart, CreateOrder, ViewOrders,
ViewOrderItems, CancelOrder, ConfirmCancelOrder
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("register/", Regsiter.as_view(), name="register"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"), 
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
    path("cart/items/", ViewCartItems.as_view(), name="cart_items"),
    path("cart/update/", UpdateCart.as_view(), name="update_cart"),
    path("cart/delete/", DeleteCart.as_view(), name="delete_cart"),
    path("order/", CreateOrder.as_view(), name="order"),
    path("order/list/", ViewOrders.as_view(), name="order_list"),
    path("order/<int:order_id>/items/", ViewOrderItems.as_view(), name="order_items"),
    path("order/<int:order_id>/cancel/", CancelOrder.as_view(), name="cancel_order"),
    path("order/<int:order_id>/cancel/confirm/", ConfirmCancelOrder.as_view(), name="confirm_cancel_order"),
]