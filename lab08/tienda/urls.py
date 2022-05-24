from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^tienda/$', views.JSONResponse.serie_list),

]
