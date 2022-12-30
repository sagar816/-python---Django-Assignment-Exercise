from django.shortcuts import render, HttpResponse, redirect
from todoapp.models import Company_Task

def delete(request, rid):
    t1=Company_Task.objects.get(id=rid)
    t1.delete()
    return redirect('/dashboard')

def edit(request, rid):
    if request.method=="POST":
        ut=request.POST['title']
        udet=request.POST['detail']
        ucat=request.POST['cat']
        udate=request.POST['date']

        t1=Company_Task.objects.filter(id=rid)
        t1.update(title=ut, detail=udet, cat=ucat, date=udate)
        return redirect('/dashboard')




    rec=Company_Task.objects.filter(id=rid)
    content={}
    content['data']=rec
    return render(request, 'editform.html', content)


def dashboard(request):
    if request.method=='POST':
        t=request.POST['title']
        det=request.POST['detail']
        cat=request.POST['cat']
        dt=request.POST['date']

        t1=Company_Task.objects.create(title=t, detail=det, cat=cat, date=dt, is_deleted='N')
        #inserrt into
        t1.save()
        return redirect('/dashboard')
        #return HttpResponse("IN POST")
    else:
        records=Company_Task.objects.all()
        content={'data':records}
        return render(request, 'dashboard.html', content)

def mumbai(request):
    records=Company_Task.objects.filter(detail="Mumbai")
    content={}
    content['data']=records
    return render(request, 'dashboard.html', content)

def delhi(request):
    records=Company_Task.objects.filter(detail="Delhi")
    content={}
    content['data']=records
    return render(request, 'dashboard.html', content)

def bangalore(request):
    records=Company_Task.objects.filter(detail="Bangalore")
    content={}
    content['data']=records
    return render(request, 'dashboard.html', content)