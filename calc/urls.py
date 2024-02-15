from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index),
    path('tmp:<int:id>', tmp),
    re_path(r'^re_tmp/(?P<year>[0-9]{4})/', re_tmp)
]