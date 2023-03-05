from django.shortcuts import render

import stripe 
from django.contrib.auth.models import Permission

from django.views.generic.base import TemplateView
from django.conf import settings

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'
#The get_context_data method is called when the view is accessed with a GET request. 
#This method adds the Stripe API publishable key to the context dictionary, which is then passed to the template when it's rendered.
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        #This value is used by the Stripe JavaScript library to initialize the Stripe payment form on the client-side.
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    #get the permission
    permission = Permission.objects.get(codename='special_status')
    #get User
    u = request.user
    #add to User's permission set
    u.user_permissions.add(permission)

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=1290,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
        return render(request,'orders/charge.html')