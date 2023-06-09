"""encrypter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from endtoendencryption.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home,name = 'Home'),
    path('account/register',register,name='registration'),
    path('account/login',loginfunc,name='login'),
    path('account/profile/verify',verifyprofilefunc,name = 'verify profile'),
    path('encode/',encodefunc,name = 'encode function'),
    path('decode/',decodefunc,name = 'decode function'),
    path('account/recover',recoverfunc,name = 'recover'),
    path('account/verify',verifyfunc,name = 'verify'),
    path('account/change/pass',changepass,name = 'change pass'),

    # path('decoded/',decodedfunc,name = 'decoded function'),
    path('logout',logout_view,name = 'logout function'),
] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
