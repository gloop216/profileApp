from django.shortcuts import render
from .models import*
# Create your views here.
def Home(request):
    project=Project.objects.all()
   
    context={
        'projects':project
    }
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact=Connect(name=name,email=email,subject=subject,msg=message)
        contact.save()
      

        return render(request,'index.html',context=context)

    return render(request,'index.html',context=context)
def portfoliodetails(request,slug):
    project=Project.objects.get(slug=slug)
    context={
        'project':project
    }

    return render(request,'portfolio-details.html',context=context)
def blogsingle(request):
    return render(request,'blog-single.html')