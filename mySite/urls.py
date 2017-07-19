from django.conf.urls import include, url
from django.conf.urls import admin

from . import views

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    
]