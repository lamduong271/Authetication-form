from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ArticleForm
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
        login(request, my_user)
        return render(request, 'authen/success.html')


class ViewUser(LoginRequiredMixin,View):
    login_url="/login/"
    def get(self,request):
        return HttpResponse("This is view:  user")

@decorators.login_required(login_url='/login/')
def view_product(request):
    return HttpResponse("this is view product")

class AddArticle(LoginRequiredMixin,View):
    login_url="/login/"
    def get(self,request):
        f = ArticleForm
        context = {"form":f}
        return render(request, 'authen/article_form.html', context)
    def post(self,request):
        form = ArticleForm(request.POST)
        print(request.user.get_all_permissions())
        if not form.is_valid():
            return HttpResponse("Invalid input")
        if request.user.has_perm('authen.add_article'):
            form.save()
        else:
            return HttpResponse("Permission denied")
        return HttpResponse("OK")




