from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices

def home(request):
    listings = Listing.objects.order_by('-created_at').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,

    }


    return render(request, 'pages/home.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    # Get seller of the month
    sellers = Realtor.objects.all().filter(is_seller=True)

    context = {
        'realtors': realtors,
        'sellers': sellers
    }
    return render(request, 'pages/about.html', context)

