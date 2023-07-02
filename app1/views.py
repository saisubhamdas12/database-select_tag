from django.shortcuts import render
# Create your views here.
from app1.models import*
from django.http import HttpResponse
# Create your views here.
def display_topic(request):
    if request.method=='POST':
        tn=request.POST['un']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()

        return HttpResponse('TOPIC DATA UPDATE')
    return render(request,'file_forms.html')

# def display_Webpage(request):
#     if request.method=='POST':
#         # tn=request.POST['un']
#         lto=Topic.objects.all()
#         d={'lto':lto}
#         name=request.POST['web']
#         url=request.POST['ur']
        
#         To=Topic.objects.get(topic_name=tn)
#         To.save()   
#         wo=Webpage.objects.get_or_create(topic_name=To,name=name,url=url)[0]
#         wo.save()
#         return HttpResponse('WEBPAGE UPDATE')
#     return render(request,'Webpage.html'd)
    

def display_Webpage(request):
    lto=Topic.objects.all()
    d={'lto':lto}
        
    if request.method=='POST':
        tn=request.POST['nic']
        name=request.POST['web']
        url=request.POST['ur']
        
        To=Topic.objects.get(topic_name=tn)  
        wo=Webpage.objects.get_or_create(topic_name=To,name=name,url=url)[0]
        wo.save()
        return HttpResponse('data is inserted')
    return render(request,'Webpage.html',d)

def display_access(request):
    
    if request.method=='POST':
        tn=request.POST['un']
        name=request.POST['web']
        url=request.POST['ur']
        date=request.POST['dt']
        author=request.POST['au']
        To=Topic.objects.get(topic_name=tn)
        To.save()
        wo=Webpage.objects.get(topic_name=To,name=name,url=url)
        wo.save()
        ar=Access.objects.get_or_create(date=date,name=wo,author=author)[0]
        ar.save()

        return HttpResponse( 'ACESS UPDATE')
    return render(request,'access.html')