from django.urls import path

from .views import *

app_name = "core"

urlpatterns = [
    path('', banner_section, name='banner_section'),
    path('mobile', banner_section_mobile, name='banner_section_mobile'),
]
