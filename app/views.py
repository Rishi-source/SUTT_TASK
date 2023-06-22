from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User 
from app.models import register_table ,appointment
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from app.forms import appointment_form 
from datetime import datetime
from django.core.mail import EmailMessage
from google.oauth2 import id_token
from django.contrib.auth.models import User
from django_tables2 import SingleTableView , RequestConfig
from app.tables import UserTable



def register(request):
    if "user_id"in request.COOKIES:
        uid = request.COOKIES["user_id"]
        usr = get_object_or_404(User,id=uid)
        login(request,usr)
        if usr.is_superuser:
            return HttpResponseRedirect("/admin")
        if usr.is_staff:
            return HttpResponseRedirect("/staff_dashboard")
        else :
            return HttpResponseRedirect("/accounts/profile/")
    if request.method=="POST":
        fname = request.POST["first"]
        last = request.POST["last"]
        un = request.POST["uname"]
        pwd = request.POST["password"]
        em = request.POST["email"]
        tp = request.POST["utype"]
        add = request.POST["address"]
        fie = request.POST["field"]
        
        usr = User.objects.create_user(un,em,pwd)
        usr.first_name = fname
        usr.last_name = last
        if tp=="staff": 
            usr.is_staff = True
        usr.save()

        reg = register_table(user=usr, address = add , Type_of_Doctor = fie)
        reg.save()
        return render(request,"register.html",{"status":"Mr/Miss. {} your Account created Successfully".format(fname)})
    return render(request,"register.html")


def check_user(request):
    if request.method=="GET":
        un = request.GET["usern"]
        check = User.objects.filter(username=un) 
        if len(check) == 1:
            return HttpResponse("Exists")
        else:
            return HttpResponse("Not Exists")

def user_login(request):
    if request.method=="POST":
        un = request.POST["username"]
        pwd = request.POST["password"]

        user = authenticate(username=un,password=pwd)
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin")      
            elif user.is_staff:
                if user.is_active :
                 return HttpResponseRedirect("/staff_dashboard")
                else:
                    pass
            else:
                 return HttpResponseRedirect("/patient_dashboard")
            

        else:
            return render(request,"register.html",{"status":"Invalid Username or Password"})

    return HttpResponse("Called")
@login_required
def patient_dashboard(request):
    return render(request,"patient_dashboard.html")
@login_required
def edit_profile(request):
    context = {}
    if request.method=="POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]
        age = request.POST["age"]
        ct = request.POST["city"]
        gen = request.POST["gender"]
        occ = request.POST["occ"]
        hoi = request.POST.get("hoi")
    usr = User.objects.filter(id=request.user.id)
    if len(usr) == 0:
         usr.first_name = fn
         usr.last_name = ln
         usr.email = em
         usr.save()

         reg = register_table(user= usr , address = hoi , age = age , occupation = occ , gender = gen , city = ct  )
         reg.save()

         if "image" in request.FILES:
            img = request.FILES["image"]
            data = register_table(profile_pic = img)
            data.save()
    else:
     if request.method=="POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]
        age = request.POST["age"]
        ct = request.POST["city"]
        gen = request.POST["gender"]
        occ = request.POST["occ"]
        hoi = request.POST.get("hoi")

        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        usr.save()

        data.age = age
        data.city = ct
        data.gender = gen
        data.occupation = occ
        data.address = hoi
        data.save()

        if "image" in request.FILES:
            img = request.FILES["image"]
            data.profile_pic = img
            data.save()

        
        context["status"] = "Changes Saved Successfully"
    return render(request,"edit_profile.html",context)
@login_required
def user_logout(request):
    logout(request)
    res =  HttpResponseRedirect("/")
    return res
def create_appointment(request):
    context = {}
    form = appointment_form()
    if request.method == "POST":
        form = appointment_form(request.POST) 
        if form.is_valid():
            data = form.save(commit=False)
            usr = User.objects.get(username=request.user.username)
            data.user = usr
            data.save()
            context["status"] = "Dear {},\nYour appointment has been successfully registered.\n Please wait for it to be approved by the doctor.".format(data.name)
    context["form"] = form
    return render(request, "appointment.html", context)
def appointment_status(request):
    context = {}
    appointments = appointment.objects.filter(user__id=request.user.id).order_by("-id")
    context = {'appointments': appointments}    
    return render(request,"appointment_status.html",context)
@login_required
def staff_dashboard(request):
    context = {}
    check = register_table.objects.filter(id=request.user.id)
    if len(check)>0:
        data = register_table.objects.get(user__id=request.user.id)
        context["data"] = data
    return render(request,"staff_dashboard.html",context)
def staff_edit_profile(request):
    context = {}
    if request.method=="POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]
        age = request.POST["age"]
        ct = request.POST["city"]
        gen = request.POST["gender"]
        occ = request.POST["occ"]
        hoi = request.POST.get("hoi")
    usr = User.objects.filter(id=request.user.id)
    if len(usr) == 0:
         usr.first_name = fn
         usr.last_name = ln
         usr.email = em
         usr.save()

         reg = register_table(user= usr , address = hoi , age = age , occupation = occ , gender = gen , city = ct  )
         reg.save()

         if "image" in request.FILES:
            img = request.FILES["image"]
            data = register_table(profile_pic = img)
            data.save()
    else:
     if request.method=="POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]
        age = request.POST["age"]
        ct = request.POST["city"]
        gen = request.POST["gender"]
        occ = request.POST["occ"]
        hoi = request.POST.get("hoi")

        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        usr.save()

        data.age = age
        data.city = ct
        data.gender = gen
        data.occupation = occ
        data.address = hoi
        data.save()

        if "image" in request.FILES:
            img = request.FILES["image"]
            data.profile_pic = img
            data.save()

        
        context["status"] = "Changes Saved Successfully"
    return render(request,"staff_edit_profile.html",context)
def staff_appointment(request):
    context = {}
    try:
        type_of_doctor = request.GET.get('Type_of_Doctor')
        data = appointment.objects.filter(details__Type_of_Doctor=type_of_doctor)
        context["data"]=data
    except register_table.DoesNotExist:
        pass
    return render(request, "staff_appointment.html", context)
def approve(request):
    context = {}
    try:
        app_id = request.GET.get('aid')
        app = appointment.objects.get(id=app_id)
        app.status = True
        app.save()
    except appointment.DoesNotExist:
        pass
    return HttpResponseRedirect("/staff_appointment")
def patient_info(request):
    user = User.objects.all()
    table = UserTable(user)
    RequestConfig(request).configure(table)
    return render(request, "patient_info.html", {'table': table})


