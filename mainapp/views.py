
from django.shortcuts import render

def home(request):
    products = {"Cherries","Apples","Oranges","Strawberries","Pears","Watermelons"}

    context= {
        'Products':products,

    }
    return render(request,"home.html",context)


