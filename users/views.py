from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

#def index(request):
    #return HttpResponse("Home")
#def login(request):
    #return HttpResponse('welcome to login page')
#def registration(request):
    #return HttpResponse('registration page')


class Indexview(View):
    def get(self,request):
        return render(request,"login.html")

class Registrationview(View):
    def get(self,request):
        return render(request,"registration.html")
    def post(self,request):
        print(request.POST.get("f_name"))
        print(request.POST.get("l_name"))
        print(request.POST.get("e_mail"))
        print(request.POST.get("d_birth"))
        print(request.POST.get("pwd"))
        print(request.POST.get("gender"))

        return render(request,"registration.html")

