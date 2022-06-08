"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from main.views import *
from django.views.static import serve
from mysite import settings

urlpatterns = [
    path('', indexHandler),
    path('services/', serviceHandler),
    path('privacy-and-policy/', privacy_policyHandler),
    path('my-account/', my_accountHandler),
    path('login/', loginHandler),
    path('frequently-asking-questions/', faqHandler),
    path('contacts/', contactHandler),
    path('compare/', compareHandler),
    path('coming-soon/', coming_soonHandler),
    path('about/', aboutHandler),
    path('error/', errorHandler),
    path('checkout/', checkoutHandler),
    path('cart/', cartHandler),
    path('wishlist/', wishlistHandler),
    path('products/', shopHandler),
    path('blogs/', blogHandler),
    path('products/<int:product_id>', productHandler),
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    })
]
