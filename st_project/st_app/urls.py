
from . import views
from django.urls import path


urlpatterns = [
    path('',views.loginuser,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('logout/',views.signout,name='logout'),
    path('games/',views.games,name='games'),



]
