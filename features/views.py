from django.shortcuts import render, redirect

from django.http import HttpResponse

from models import *
from datetime import datetime

def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")

def reset(request):
    john = Customer.objects.get(pk=1)
    jane = Customer.objects.get(pk=2)

    john.last_viewed_feature = datetime.strptime('2015-03-01 19:10:00', '%Y-%m-%d %H:%M:%S')
    jane.last_viewed_feature = datetime.strptime('2015-05-07 19:05:00', '%Y-%m-%d %H:%M:%S')

    john.save()
    jane.save()

    return redirect('index')


def customer(request):
    all_customers = Customer.objects.all()
    return render(request, 'customers.html', {
        'customers': all_customers
    })

def customer_detail(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)

    new_features = Feature.objects.filter(date__gte=customer.last_viewed_feature).count()

    return render(request, 'customer_detail.html', {
        'customer': customer,
        'features': new_features
    })

def new_features(request, customer_id):

    customer = Customer.objects.get(pk=customer_id)
    new_features = Feature.objects.filter(date__gte=customer.last_viewed_feature)

    old_last_viewed_feature = customer.last_viewed_feature

    now = datetime.now()
    customer.last_viewed_feature = now
    customer.save()

    # Set customer last viewed features

    return render(request, 'new_features.html', {
        'customer': customer,
        'last_viewed_feature': old_last_viewed_feature,
        'features': new_features
    })
