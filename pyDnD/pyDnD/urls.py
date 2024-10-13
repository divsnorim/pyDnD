from django.urls import path, include

from skibidi_app.views import pageNotFound

urlpatterns = [
    path('', include('skibidi_app.urls'))
]

handler404 = pageNotFound