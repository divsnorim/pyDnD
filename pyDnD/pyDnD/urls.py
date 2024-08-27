
from django.urls import path, include
from cocojumbo.views import index

urlpatterns = [
    path('', index, name='home'),
    path('haze_part/', include('skibidi_app.urls'))
]
