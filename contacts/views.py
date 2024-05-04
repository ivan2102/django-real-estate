from django.shortcuts import redirect, render
from . models import Contacts
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name= request.POST['name']
        email= request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has already made inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            contacted = Contacts.objects.all().filter(listing_id=listing_id, user_id=user_id)

            if contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)



        contact = Contacts(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        #send_mail(
           # 'Contact for Property Listing',
           # 'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
           # 'iradisavljevic168@gmail.com',
           # [realtor_email, 'iradisavljevic168@gmail.com'],
           # fail_silently=False
       # )
        messages.success(request, 'Your request has been submitted, a realtor will contact you soon')
        return redirect('/listings/'+listing_id)
    return render(request, 'listings/listing.html')
