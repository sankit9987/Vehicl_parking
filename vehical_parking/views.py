from django.shortcuts import render,redirect
from .form import userlogin
from django.contrib.auth import authenticate, login, logout
from .models import category,vehical
import random
from django.db.models import Q
from datetime import datetime,timedelta,time
# Create your views here.
def index(request):
    fm = userlogin()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = userlogin(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('adminpage.html')
            else:
                return render(request, 'index.html')
    else:
        return redirect('adminpage')
    return render(request,'index.html', {'form': fm})
def ulogout(request):
    logout(request)
    return redirect('index')
def adminpage(request):
    if request.user.is_authenticated:
        today = datetime.now().date()
        yesterday = today-timedelta(1)
        last = today - timedelta(7)
        tv = vehical.objects.filter(pdate=today).count()
        yv = vehical.objects.filter(pdate=yesterday).count()
        ls = vehical.objects.filter(pdate__gte=last, pdate__lte=today).count()
        todayv = vehical.objects.all().count()
        d = {'tv':tv,'yv':yv,'ls':ls,'todayv':todayv}
        return render(request, 'adminpage.html',d)
    else:
        return redirect('index')
def Addcatgroy(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ct = request.POST['ct']
            category.objects.create(categoryname=ct)
            return redirect('managecategroy')
    else:
        return redirect('index')
    return render(request, "addcatgroy.html")
def managecategroy(request):
    if request.user.is_authenticated:
        categor = category.objects.all()
        d = {'category': categor}
        return render(request,"managecategroy.html",d)
    else:
        return redirect('index')
def deletecategory(request,id):
    if request.user.is_authenticated:
        categor = category.objects.get(id=id)
        categor.delete()
        return redirect('managecategroy')
    else:
        return redirect('index')
def addvehicle(request):
    if not request.user.is_authenticated:
        return redirect('index')
    categor = category.objects.all()
    d = {'category': categor}
    if request.method == "POST":
        pk = random.randint(00000000, 99999999)
        ct = request.POST['categor']
        vc = request.POST['vc']
        on = request.POST['on']
        oc = request.POST['oc']
        status = "In"
        categor=category.objects.get(categoryname=ct)
        vehical.objects.create(parkingnumber=pk, category=categor, vehicalcompony=vc, ownername=on, ownercontact=oc, outtime="", parkingcharge="", status=status)
        return redirect("manageinvehicle")
    return render(request, "Addvehicle.html", d)
def manageinvehicle(request):
    if request.user.is_authenticated:
        ve=vehical.objects.filter(status="In")
        return render(request,"manageinvehicle.html",{'vehicle':ve})
    else:
        return redirect('index')
def editinvehical(request,id):
    if request.user.is_authenticated:
        ve = vehical.objects.get(id=id)
        if request.method == "POST":
            ot = request.POST['ot']
            pc = request.POST['pc']
            status = "Out"
            vehical.objects.filter(id=id).update(outtime=ot,parkingcharge=pc,status=status)
            return redirect("manageoutvehicle")
        return render(request,"editinvehical.html",{'ve':ve})
    else:
        return redirect('index')
def manageoutvehicle(request):
    if request.user.is_authenticated:
        ve=vehical.objects.filter(status="Out")
        return render(request,"manageoutvehical.html",{'vehicle':ve})
    else:
        return redirect('index')
def viewcustomerdetails(request,id):
    if request.user.is_authenticated:
        ve = vehical.objects.get(id=id)
        return render(request,"viewcustomerdetails.html",{'ve':ve})
    else:
        return redirect('index')
def datesearch(request):
    if request.user.is_authenticated:
        return render(request,"datesearch.html")
    else:
        return redirect('index')
def datesearchresult(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fd = request.POST['fd']
            td = request.POST['td']
            ve = vehical.objects.filter(Q(pdate__gte=fd) & Q(pdate__lte=td))
            return render(request,"datesearchresult.html",{'ve':ve,'fd':fd,'td':td})
        return render(request,"datesearchresult.html")
    else:
        return redirect('index')