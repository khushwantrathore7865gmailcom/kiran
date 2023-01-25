"""orackel URL Configuration

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
from django.urls import path
from product.views import home, prodList, prodDesc, inquiry, aboutus, contactus, requestforsample, customization, paid
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home, name='home'),
                  path('category/<int:category>', prodList, name='prodList'),
                  path('product/<int:prod>', prodDesc, name='prodDesc'),
                  path('inquiry/<int:prod>', inquiry, name='inquiry'),
                  path('sample/<int:prod>', requestforsample, name='sample'),
                  path('custom/<int:prod>', customization, name='custom'),
                  path('pay/<int:prod>', paid, name='paid'),
                  path('aboutUs/', aboutus, name='aboutus'),
                  path('contactus/', contactus, name='contactus')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
