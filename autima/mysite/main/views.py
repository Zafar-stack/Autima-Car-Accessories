from django.shortcuts import render
from main.models import *

# Create your views here.


def indexHandler(request):

    return render(request, 'indexes/index.html', {})


def serviceHandler(request):

    return render(request, 'service.html', {})


def privacy_policyHandler(request):

    return render(request, 'privacy-policy.html', {})


def my_accountHandler(request):

    return render(request, 'my-account.html', {})


def loginHandler(request):

    return render(request, 'login.html', {})


def faqHandler(request):

    return render(request, 'faq.html', {})


def contactHandler(request):

    return render(request, 'contact.html', {})


def compareHandler(request):

    return render(request, 'compare.html', {})


def coming_soonHandler(request):

    return render(request, 'coming-soon.html', {})


def aboutHandler(request):

    return render(request, 'about.html', {})


def errorHandler(request):

    return render(request, '404.html', {})


def checkoutHandler(request):

    return render(request, 'checkout.html', {})


def cartHandler(request):

    return render(request, 'cart.html', {})


def wishlistHandler(request):

    return render(request, 'wishlist.html', {})


def shopHandler(request):

    return render(request, 'shoplists/shop-right-sidebar.html', {})


def blogHandler(request):

    return render(request, 'blogs/blog.html', {})


def productHandler(request, product_id):

    return render(request, 'products/product-details.html', {})