from django.urls import path, include
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('bank',views.bank,name='bank'),
    path('logout',views.logout,name='logout'),
]