"""ZappyFoodProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from ZappyFoodApp import views
from django.conf.urls.static import static
from django.conf.urls.static import settings
app_name='zappyapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homeView),
    path('signup/',views.signupview),
    path('allproduct/',views.allview),
    path('about/',views.about),
    path('home/', views.home, name='imageupload'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/',views.home),
    path('cart',views.cart),
    path('cartdel',views.cartdelelete),

    path('viewcart',views.viewCart),
    path('profile',views.profile),
    path('updateprofile',views.customer),
    path('cart_home/',views.cart_home),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
