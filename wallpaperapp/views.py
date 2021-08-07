from django.shortcuts import render
from .models import Image
from .forms import ImageForm
# Create your views here.

def Index(request):
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=ImageForm()
    wallpaer=Image.objects.all()
    context={
        'form':form,
        'image':wallpaer,
    }
    return render(request,'wallpaperapp/index.html',context)