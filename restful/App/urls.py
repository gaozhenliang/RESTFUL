from django.conf.urls import url
from .views import views
#格式后缀
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #GET /students
    #POST /students/
    url(r'^students/$',views.StudentsList.as_view()),  #as_view()的目的是让它作为视图来用
    #GET /students/id
    #PUT /students/id
    #DELETE /students/id
    url(r'^students/(?P<pk>\d+)/$', views.StudentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)