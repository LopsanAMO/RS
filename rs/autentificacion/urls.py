from django.conf.urls import url
from .views import Registro, Login

urlpatterns = [
    url(r'^login/', Login.as_view()),
    url(r'^registro/', Registro.as_view()),
]
