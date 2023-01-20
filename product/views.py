import datetime

from django.shortcuts import render

from .models import Categories, Product, OrderHistory, Inquiry, Customization, Requestforsample, Contact, \
    Talk_to_Analyst


# Create your views here.
def home(request):
    c = Categories.objects.all()
    order = OrderHistory.objects.all()
    return render(request, 'index.html', {'cat': c})


def aboutus(request):
    c = Categories.objects.all()
    order = OrderHistory.objects.all()
    return render(request, 'AboutUs.html', {'cat': c})


def contactus(request):
    c = Categories.objects.all()
    if request.method == 'POST':
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        desc = request.POST.get("desc", "")
        date = datetime.datetime.now()
        company = request.POST.get("company")
        country = request.POST.get("country")
        designation = request.POST.get("designation")
        inq = Contact(email=email, phone=phone, first_name=first_name, last_name=last_name, desc=desc, date=date,
                      company=company, country=country, designation=designation)
        inq.save()

    return render(request, 'ContactUs.html', {'cat': c})


def prodList(request, category):
    c = Categories.objects.all()
    cat = Categories.objects.get(pk=category)
    prod = Product.objects.filter(category=cat)
    return render(request, 'AdvanceMaterial.html', {'prod': prod, 'cat': c})


def prodDesc(request, prod):
    c = Categories.objects.all()
    p = Product.objects.get(pk=prod)
    if request.method == 'POST':
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        desc = request.POST.get("desc", "")
        date = datetime.datetime.now()
        company = request.POST.get("company")
        country = request.POST.get("country")
        designation = request.POST.get("designation")
        inq = Talk_to_Analyst(email=email, phone=phone, first_name=first_name, last_name=last_name, desc=desc,
                              date=date,
                              company=company, country=country, designation=designation, prod=p)
        inq.save()
    return render(request, 'Industrial.html', {'prod': p, 'cat': c})


def inquiry(request, prod):
    c = Categories.objects.all()
    p = Product.objects.get(pk=prod)
    if request.method == 'POST':
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        desc = request.POST.get("desc", "")
        date = datetime.datetime.now()
        company = request.POST.get("company")
        country = request.POST.get("country")
        designation = request.POST.get("designation")
        inq = Inquiry(email=email, phone=phone, first_name=first_name, last_name=last_name, desc=desc, date=date,
                      company=company, country=country, designation=designation, prod=p)
        inq.save()

    return render(request, 'inquiry.html', {'p': p, 'cat': c})


def customization(request, prod):
    c = Categories.objects.all()
    p = Product.objects.get(pk=prod)
    if request.method == 'POST':
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        desc = request.POST.get("desc", "")
        date = datetime.datetime.now()
        company = request.POST.get("company")
        country = request.POST.get("country")
        designation = request.POST.get("designation")
        custo = Customization(email=email, phone=phone, first_name=first_name, last_name=last_name, desc=desc,
                              date=date,
                              company=company, country=country, designation=designation, prod=p)
        custo.save()

    return render(request, 'custom.html', {'prod': p, 'cat': c})


def requestforsample(request, prod):
    c = Categories.objects.all()
    p = Product.objects.get(pk=prod)
    if request.method == 'POST':
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        desc = request.POST.get("desc", "")
        date = datetime.datetime.now()
        company = request.POST.get("company")
        country = request.POST.get("country")
        designation = request.POST.get("designation")
        rfs = Requestforsample(email=email, phone=phone, first_name=first_name, last_name=last_name, desc=desc,
                               date=date,
                               company=company, country=country, designation=designation, prod=p)
        rfs.save()
    return render(request, 'sample.html', {'p': p, 'cat': c})
