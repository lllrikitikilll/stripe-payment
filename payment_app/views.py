from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpRequest
from django.views import View
from stripe_payment.settings import STRIPE_SECRET_KEY
import stripe

YOUR_DOMAIN = 'http://127.0.0.1:8000'
stripe.api_key = STRIPE_SECRET_KEY

# Create your views here.
class CreateCheckoutSession(View):

    def get(self, request: HttpRequest, *args, **kwargs):

        checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': 2000,
                            'product_data': {
                                'name': 'Test_item',
                                'description': 'Whaaat?'

                            },
                        },
                        'quantity': 1
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success.html',
                cancel_url=YOUR_DOMAIN + '/cancel.html',
            )

        # return redirect(checkout_session.url)
        return JsonResponse({'id': checkout_session.id})