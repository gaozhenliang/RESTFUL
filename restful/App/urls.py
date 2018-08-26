from django.conf.urls import url
from .views import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
]