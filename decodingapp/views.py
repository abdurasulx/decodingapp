from django.shortcuts import render

def home(request):
    src=request.POST
    return render(request,'index.html',{'login':'banda','pass':'bandacap'})
# Create your views here.
