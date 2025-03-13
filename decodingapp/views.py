from django.shortcuts import render
from .models import *

def home(request):
    src=request.POST
    svl=Savol.objects.all()
    for i in src:
        print(src[i],'kuku')
    return render(request,'index.html',{'login':'banda','pass':'bandacap','ques':svl})
def seeque(request,slug):
    ans=request.POST.get('answer')
    src=''
    try: 
        src=Savol.objects.get(id=slug)
    except:
        src=''

    
    if src!='':
        if not ans:
            ans=''
            return render(request,'post.html',{'login':'banda','pass':'bandacap','savol':src,'a':ans,'correct':'1'})
        else:
            if ans==src.answer:
                return render(request,'post.html',{'login':'banda','pass':'bandacap','savol':src,'a':ans,'correct':'2'})
            if ans!=src.answer:
                return render(request,'post.html',{'login':'banda','pass':'bandacap','savol':src,'a':ans,'correct':'3'})


        
        
    else:
        return render(request,'404.html')
# Create your views here.
