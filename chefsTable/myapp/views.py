from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import InputForm
# from .forms import LogForm
# Create your views here.
def home(request):
    return HttpResponse("Welcome to Little Lemon Restaurant")

def display_date(request):
    date_joined=datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text="""<h1 style="color: #F4CE14;"> This is little lemon again!</h1"""
    return HttpResponse(text)
def menu_item(request,dishname):
    items= {
        "pasta":"italian dish",
        "falafel":"arabic food",
        "biriyani":"indian food",
    }
    description=items[dishname]
    return HttpResponse(f"<h1>{dishname} </h1>"+description )# contains html heading and a plain text

def test(request):
    path=request.path
    scheme= request.scheme
    method=request.method
    address=request.META['REMOTE_ADDR']
    user_agent=request.META['HTTP_USER_AGENT']
    path_info=request.path_info
    return HttpResponse(path_info)

def form_view(request):
    form=InputForm()
    context={"form":form}
    return render(request,'home.html',context)

# def Logger_view(request):
#     form=LogForm()
#     if request.method=="POST":
#         form=LogForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context={"form":form}
#     return render(request,'home.html',context)