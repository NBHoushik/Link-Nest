from django.urls import path
from . import views
urlpatterns = [
  path('',views.home),
  path("index/",views.index, name="index"),
  path('signup/',views.signup,name="signup"),
  path("profile_check/",views.profile_check,name="profile_check"),
  path("register_user/",views.register_user,name="register_user"),
  path("add_link_page/<str:username>/",views.add_link_page,name="add_link_page"),
  path("profile_page/<str:username>/",views.profile_page,name="profile_page"),
  path("add_link/<str:username>/",views.add_link,name="add_link"),
  path("delete_update/<int:link_id>/",views.delete_update,name="delete_update"),
  path("update/<int:link_id>/",views.update,name="update"),
  path("u/<str:username>/",views.link_nest,name="link_nest"),
  path("qr_code/<str:username>/",views.qr_code,name="qr_code"),
  path('profileImage/<str:username>',views.profileImage,name="profileImage"),
]