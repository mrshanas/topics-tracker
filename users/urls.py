from django.urls import path
# from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name='login'),
    #Logout url
    path('logout/',views.logout_view,name='logout_view'),
    # url(r'^login/$',login,{'template_name':'users/login.html'},name=login),

    # the register view
    path('register/',views.register,name='register'),
]