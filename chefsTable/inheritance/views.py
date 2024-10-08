from django.shortcuts import render

def home2(request):
    return render(request,'home2.html')

def about2(request):
    return render(request,'about2.html')

def menu2(request):
    return render(request,'menu2.html')
