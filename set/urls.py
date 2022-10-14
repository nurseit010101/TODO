"""set URL Configuration

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
from django.conf.urls.static import static
from set.settings import MEDIA_ROOT, MEDIA_URL
from set_app.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('edit/<int:id>', update, name = 'update'),

    path('card/', card, name = 'card'),

    path('delete/<int:id>', delete_letter, name = 'delete'),
    path('card/delete_card/<int:id>', delete_card, name = 'delete'),

    path('card/w_card/<int:id>', w_card, name = 'delete'),

    path('izbran/', izbran, name = 'izbran'),
    path('izbran_letter/<int:id>', izbran_letter, name = 'izbran_letter'),
    path('izbran/izbran_delete/<int:id>', izbran_delete, name = 'izbran_delete'),

]

urlpatterns += static(MEDIA_URL, Document_root = MEDIA_ROOT) 

