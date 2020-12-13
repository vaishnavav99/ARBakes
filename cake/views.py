from django.shortcuts import render
from .models import Cake,Special

# Create your views here.
def handler404(request,exception):
    return render(request,"404.html",{'x':True,'page':'Oops!!'})

def index(request):

    styles= Cake.objects.values('style').distinct()
    cakes= Cake.objects.all()
    special= Special.objects.all()
    

    return render(request,"index.html",{'cakes':cakes ,'special': special,'styles':styles,'page':'Home'})


def contact(request):
    return render(request,"contact.html")

def menu(request):
    cakes= Cake.objects.all()
    styles= Cake.objects.values('style').distinct()
    
    return render(request,"menu.html",{'cakes':cakes ,'styles':styles ,'page':'Menu'})

