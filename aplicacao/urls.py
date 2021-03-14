from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import views

urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^refresh-token/', refresh_jwt_token),
    url(r'^usuario/$', views.UsuarioList.as_view(), name='usario-list'),
]