from django.urls import path
from .views import *

urlpatterns = [
    path('signup', Signup.as_view()),
    path('login', Login.as_view()),
    path('user', User_view.as_view()),
    path('user/<int:id>', malik.as_view()),
    path('logout', Logout.as_view()),
    path('upload/',upload_file.as_view()),
    path('Edit_Profile',Edit_Profile.as_view()),
    path('subscribe',Subscribe.as_view()),
    path('adminlogin',Admin.as_view()),
    path('adminuser',AdminUser.as_view()),
    path('usersData',Usersdata.as_view()),
    path('superuser',Make_superuser.as_view()),
    path('deleteuser',Delete_user.as_view()),
    path('searchuser',Search_user.as_view()),

    # ==================================


]
