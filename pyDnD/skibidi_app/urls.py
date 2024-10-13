from django.urls import path, re_path
from skibidi_app.views import *

urlpatterns = [
    path('', index, name="home"),
    path('cats/<int:cat>/', cats),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)  # регулярное выражение /archive/годиз4чисел/
]
