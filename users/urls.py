from django.urls import path
from users import views

urlpatterns=[
    #path('index',views.index),
    #path('login',views.login),
    #path('registration',views.registration)
    path('login',views.Indexview.as_view()),
    path('registration',views.Registrationview.as_view())

]

