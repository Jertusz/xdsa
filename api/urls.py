from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
        path('products/', views.ProductList.as_view()),
        path('products/create', views.ProductCreate.as_view()),
        path('products/<int:pk>', views.ProductDetail.as_view()),
        path('products/<int:pk>/modify', views.ProductModify.as_view()),

        path('orders/', views.OrderList.as_view()),
        path('orders/<int:pk>', views.OrderDetail.as_view()),
        path('orders/<int:pk>/modify', views.OrderModify.as_view()),
        path('orders/create', views.OrderCreate.as_view()),

        path('users/', views.UserList.as_view()),
        path('users/register', views.UserRegister.as_view()),
        path('users/<int:pk>/', views.UserDetail.as_view()),
        path('users/<int:pk>/orders', views.UserOrderList.as_view()),
        path('users/<int:pk>/modify', views.AdminModifyUser.as_view()),
        path('users/<int:pk>/settings', views.UserModifyUser.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
        path('api-auth/', include('rest_framework.urls')),
        ]
