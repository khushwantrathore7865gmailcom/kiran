import datetime
import pandas as pd
from django.shortcuts import render, redirect

from .models import Categories, Product, OrderHistory, Inquiry, Customization, Requestforsample, Contact, \
    Talk_to_Analyst, Paid_product
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q


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
        send_mail(
            subject="contacted",
            message=email + " wants to contact you" + "\n message::" + desc,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['sales@oraclemarketinsights.com'])

    return render(request, 'ContactUs.html', {'cat': c})


def prodList(request, category):
    c = Categories.objects.all()
    cat = Categories.objects.get(pk=category)
    prod = Product.objects.filter(category=cat)
    return render(request, 'AdvanceMaterial.html', {'prod': prod, 'cat': c, 'c': cat})


def prodDesc(request, prod):
    c = Categories.objects.all()
    p = Product.objects.get(pk=prod)
    ap = Product.objects.filter(~Q(pk=prod))
    if len(ap) > 3:
        a = ap[:3]
    else:
        a = ap
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
        send_mail(
            subject="Request to talk to analyst for product" + p.name,
            message=email + " wants to contact you" + "\n message::" + desc,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['sales@oraclemarketinsights.com'])
        return redirect('/product/' + p.pk)
    return render(request, 'Industrial.html', {'prod': p, 'cat': c, 'plist': a})


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
        send_mail(
            subject="Inquiry for product" + p.name,
            message=email + " wants to contact you" + "\n message::" + desc,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['sales@oraclemarketinsights.com'])
        return redirect('/product/' + p.pk)

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
        send_mail(
            subject="Customization request for product" + p.name,
            message=email + " wants to contact you" + "\n message::" + desc,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['sales@oraclemarketinsights.com'])
        return redirect('/product/' + p.pk)

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
        send_mail(
            subject="Sample request for product" + p.name,
            message=email + " wants to contact you" + "\n message::" + desc,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['sales@oraclemarketinsights.com'])
        return redirect('/product/' + p.pk)

    return render(request, 'sample.html', {'p': p, 'cat': c})


def paid(request, prod):
    c = Categories.objects.all()
    p = Product.objects.get(pk=prod)
    if request.method == 'POST':
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")

        date = datetime.datetime.now()
        company = request.POST.get("company")
        country = request.POST.get("country")
        designation = request.POST.get("designation")
        lisc = request.POST.get("license")

        rfs = Paid_product(email=email, phone=phone, first_name=first_name, last_name=last_name,
                           date=date,
                           company=company, country=country, designation=designation, lic=lisc, prod=p)
        rfs.save()
        send_mail(
            subject='Payment done for product' + p.name + 'by user' + first_name + ' ' + last_name,
            message=email + " paid for the product" + p.name,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['sales@oraclemarketinsights.com'])

        return redirect('/')
    return render(request, 'Paid_product.html', {'prod': p, 'cat': c})


def savedata(request):
    dfs = pd.read_excel('E:\kiran\orackel\static\data.xlsx')
    print(dfs.columns)
    for i in dfs.index:
        d = dfs['Description'][i]
        try:
            c = Categories.objects.get(name=dfs['Category'][i].strip().strip(':'))
        except:
            if dfs['Category'][i].strip().strip(':') == 'Semiconductor':
                c = Categories.objects.get(name='Semiconductors')
            if dfs['Category'][i].strip().strip(':') == 'Bulk Chemicals':
                c = Categories.objects.get(name='Bulk Chemicals & Materials')

        p = Product(name=dfs['Report Title'][i], description=d.splitlines()[0], category=c,
                    table_of_Content=dfs['Table of Contents'][i], additional=d, single_user=dfs['SINGLE USER'][i],
                    multi_user=dfs['MULTIPLE / CORPORATE'][i], cooperate_user=dfs['MULTIPLE / CORPORATE'][i],
                    data_pack=dfs['DATA PACK'][i])
        p.save()
