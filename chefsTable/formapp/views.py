from django.shortcuts import render
from formapp.forms import LogForm
from .models import food
# Create your views here.

def about(request):
    about_content={
        'about':"this page is about little lemon restaurant"
    }
    return render(request,'about.html',about_content)
# def food(request):
#     newmenu={'mains':[{'name':'falafel','price':'12'},
#                       {'name':'shawarma','price':"15"},
#                       {'name':'biriyani','price':"20"}
#                       ]     
#     }
#     return render(request,'menu.html',newmenu)

def form_view(request):
    form=LogForm()
    if request.method=="POST":
        form=LogForm(request.POST)
        if form.is_valid():
            form.save()
            form=LogForm()
    context={"form":form}
    return render(request,'home.html',context)

def menu_by_id(request):
    newmenu=food.objects.all
    new_menu_dict={'menu':newmenu}
    return render(request,'menu_card.html',new_menu_dict)