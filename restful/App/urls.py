from django.conf.urls import url
from .views import views
#格式后缀
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #GET /students
    #POST /students/
    url(r'^students/$',views.studentsList),
    #GET /students/id
    #PUT /students/id
    #DELETE /students/id
    url(r'^students/(?P<pk>\d+)/$', views.studentDetail),
]

#给路由添加后缀(添加api的后缀),  当添加此函数时，会把url按点号切割，如果是json则返回json格式的数据，
#如果是api，则会把json格式的数据传递给模板进行渲染，再返回给客户端，这些操作都是这个函数去帮我们做的
urlpatterns = format_suffix_patterns(urlpatterns)