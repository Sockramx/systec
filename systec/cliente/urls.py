from django.conf.urls import url
from .views import registrar


urlpatterns = [
    url(r'^registrar/', registrar, name='registrar')
]