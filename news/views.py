from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View
# Create your views here.
class indexClass(View):
    def get(self,request):
        return HttpResponse("hi")
class addPostClass(View):
    def get(self,request):
        form = PostForm
        return render(request,'news/add_news.html', {"form": form})
class save_news(View):
    def get(self,request):
        form = PostForm
        return render(request,'news/add_news.html', {"form": form})
    def post(self,request):
        data = PostForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse("saved!")
        else:
            return HttpResponse("Failed")
    def put(self,request):
        pass

def email_view(request):
    send_email = SendEmail()
    return render(request,'news/email.html', {"form_email":send_email})

def email_sent(request):
    if request.method=="POST":
        data = SendEmail(request.POST)
        if data.is_valid():
            title=data.cleaned_data["title"]
            cc=data.cleaned_data["cc"]
            content=data.cleaned_data["content"]
            email=data.cleaned_data["email"]
            context = {"title": title, "content":content,"email": email}
            context2 = {"data":data}
            return render(request, 'news/print_email.html', context2)
        else:
            return HttpResponse("Failed")
    else:
        return HttpResponse("not a post request")



