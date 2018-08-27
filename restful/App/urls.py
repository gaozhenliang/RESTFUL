from django.conf.urls import url
from .views import views

urlpatterns = [
    #GET /students
    #POST /students/
    url(r'^students/$',views.studentsList),
    #GET /students/id
    #PUT /students/id
    #DELETE /students/id
    url(r'^students/(?P<pk>\d+)/$', views.studentDetail),
]