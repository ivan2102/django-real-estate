from django.shortcuts import get_object_or_404, render
from . models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.
def home(request):
 listings = Listing.objects.order_by('-created_at').filter(is_published=True)
 paginator = Paginator(listings, 3)
 page = request.GET.get('page')
 paged_listings = paginator.get_page(page)

 context = {
  'listings': paged_listings
 }
 return  render(request, 'listings/listings.html', context)

def listing(request, listing_id):
 listing = get_object_or_404(Listing, pk=listing_id)

 context = {
   'listing': listing
 }
 return render(request, 'listings/listing.html', context) 

def search(request):

  query_list = Listing.objects.order_by('-created_at')

  #Keywords
  if 'keywords' in request.GET:
   keywords = request.GET['keywords']
  if keywords:
   query_list = query_list.filter(description__icontains=keywords)

  #City
  if 'city' in request.GET:
   city = request.GET['city']
  if city:
    query_list = query_list.filter(city__iexact=city)

  #State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
     query_list = query_list.filter(state__iexact=state)

  #Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      query_list = query_list.filter(bedrooms__lte=bedrooms)

  #Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      query_list = query_list.filter(price__lte=price)
 
  context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': query_list,
        'values': request.GET

 }
  return render(request, 'listings/search.html', context) 

