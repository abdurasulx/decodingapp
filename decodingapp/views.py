from django.shortcuts import render
from .models import *

def home(request):
    src=request.POST
    svl=Savol.objects.all()
    for i in src:
        print(src[i],'kuku')
    return render(request,'index.html',{'login':'banda','pass':'bandacap','ques':svl})
def seeque(request,slug):
    return 1
# Create your views here.
