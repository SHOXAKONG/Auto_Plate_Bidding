from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('plates/', views.plates, name='plates'),
    path('bids/', views.bids, name='bids'),
    path('plate_detail/<int:pk>', views.plate_detail, name='plate_detail')
]