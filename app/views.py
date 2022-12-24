from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from app.models import *

def insert_topic(request):
    if request.method=="POST":
        #tn=request.POST['topic']
        tn=request.POST.get('topic')
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('topic_name value inserted successfully')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    topics=Topic.objects.all()

    d={'topics':topics}
    if request.method=="POST":
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('insert_webpage value inserted successfully')

    return render(request,'insert_webpage.html',d)


def insert_AccessRecords(request):
    topics=Topic.objects.all()
    webpages=Webpage.objects.all()
    d={'topics':topics,'webpages':webpages}
    if request.method=="POST":
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        dt=request.POST['dt']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        A=AccessRecords.objects.get_or_create(name=W,date=dt)[0]
        A.save()
        return HttpResponse('insert_ accessrecords successfully')

    return render(request,'insert_AccessRecords.html',d)


def insert_AR(request):
    topics=Topic.objects.all()
    webpages=Webpage.objects.all()
    d={'topics':topics,'webpages':webpages}
    if request.method=="POST":
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        dt=request.POST['dt']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        A=AccessRecords.objects.get_or_create(name=W,date=dt)[0]
        A.save()
        return HttpResponse('insert_ accessrecords successfully')
    return render(request,'insert_AR.html',d)

def select_topic(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    if request.method=='POST':
        tn=request.POST.getlist('topic')
        print(tn)
        webpages=Webpage.objects.none()
        for i in tn:
            webpages=webpages|Webpage.objects.filter(topic_name=i)
        data={'webpages':webpages}
        return render(request,'display_webpage.html',data)
    return render(request,'select_topic.html',d)


def checkbox(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    return render(request,'checkbox.html',d)


def select_AccessRecords(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    if request.method=="POST":
        tn=request.POST.getlist('AR')
        print(tn)
        accessrecords=AccessRecords.objects.none()
        for i in tn:
            accessrecords=accessrecords|AccessRecords.objects.filter(id=i)
        data={'accessrecords':accessrecords}
    
        return render(request,'display_AccessRecords.html',data)
    return render(request,'select_AccessRecords.html',d)
