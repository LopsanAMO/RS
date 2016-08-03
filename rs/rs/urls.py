from django.conf.urls import url, include
from django.contrib import admin
from autentificacion.views import Home
from autentificacion import urls as urlsAuth

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^/', Home.as_view),
    url(r'^autentificacion/', include(urlsAuth, namespace='auth'))
]
