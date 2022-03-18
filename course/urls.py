from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_, name="login"),
    path('sign-up/', views.sign_up, name="sign-up"),
    path('logout/', views.logout_, name="logout"),
    path('courses/', views.courses, name="courses"),
    path('courses/<str:course>/', views.course, name="course"),
    path('registered-courses/', views.view_courses, name="registered-courses"),
    path('registered-courses/<str:course>/', views.tutorial, name="tutorial")

]