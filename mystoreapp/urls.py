from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home , name='home'),
    path('index/', views.index , name='index'),
    path('accounts/logout/',views.custlogout, name='logout'),
    path('accounts/login/', views.custlogin, name='login'),
    path('accounts/change-password/', views.custchangepassword , name='change-password'),
    path('accounts/password_reset',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html') ,name='password_reset' ),
    path('accounts/password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('accounts/reset/done',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
    path('products/', views.Productlist.as_view() , name='product_list'),
    path('product_detail/<str:prod_id>/', views.Productdetail.as_view() , name='product_detail'),
    path('product_add/', views.Productadd.as_view() , name='product_add'),
    path('product_delete/<str:prod_id>/',views.Productdelete.as_view(), name='product_delete'),
    path('product_update/<str:prod_id>/', views.Productupdate.as_view(), name='product_update'),
    path('product_update_image/<str:prod_id>/', views.Productupdateimage.as_view(), name='product_image')
]