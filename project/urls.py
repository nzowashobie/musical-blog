"""project URL Configuration

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
from django.conf.urls.static import static 
from django.conf import settings
from ninja import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('RNB/zedbeats/', include('ninja.urls')),
    path('item/', include('ninja.urls')),
    path('index/item/', include('ninja.urls')),
    #path('/<int:check_id>/' ,views.Photos),
    #path('RNB/afrobeats/', include('ninja.urls')),
    #path('RNB/zedbeats/', include('ninja.urls')),
    #path('RNB/gospel/', include('ninja.urls')),
    #path('RNB/hiphop/', include('ninja.urls')),
   # path('RNB/classics/', include('ninja.urls')),
    #path('RNB/classics/throw_back/', include('ninja.urls')),
    #path('RNB/classics/classic_rnb/', include('ninja.urls')),
    #path('RNB/classics/classic_zed/', include('ninja.urls')),
    #path('RNB/hip_hop/', include('ninja.urls')),
    #path('videos/live_performance/', include('ninja.urls')),
    #path('index/', include('ninja.urls')),
    #path('all/', include('ninja.urls')),
    path('', include('ninja.urls')), # new 
    path('biography/<str:check_id>/' ,views.check), 
    path('RNB/biography/<str:check_id>/' ,views.check), 
    path('movies/<str:name_id>/' ,views.play),
    #path('song/<int:song_id>/' ,views.player),
 
   
   
  
]+ static(settings.MEDIA_URL, 
            document_root=settings.MEDIA_ROOT)
