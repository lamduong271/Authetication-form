from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate

class IndexClass(View):
    def get(self, request):
        return HttpResponse('Hello')

# Create your views here.
class LoginClass(View):
    def get(self,request):
        return render(request,'authen/login.html')
    def post(self,request):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        my_user = authenticate(username=user_name, password=password)
        if my_user is None:
            return HttpResponse("user not exist")
        return HttpResponse("Login username and paws is %s %s"%(user_name,password))