from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^series/$', views.JSONResponse.serie_list),
    re_path(r'^series/(?P<pk>[0-9]+)/$', views.JSONResponse.serie_detail),

]
