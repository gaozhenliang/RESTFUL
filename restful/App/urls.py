from django.conf.urls import url,include
from App.views.views import StudentViewSet,UserViewSet
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students',StudentViewSet)
router.register(r'users',UserViewSet)


urlpatterns = [
    url(r'^',include(router.urls))
]


# students_list = StudentViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })
#
#
# student_detail = StudentViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'patch':'partial_update',
#     'delete':'destroy'
# })
#
# users_list = UserViewSet.as_view({
#     'get':'list'
# })
#
# user_detail = UserViewSet.as_view({
#     'get':'retrieve'
# })

# urlpatterns = format_suffix_patterns([
#     url(r'^students/$',students_list,name='students_list'),
#     url(r'^students/(?P<pk>\d+)/$',student_detail,name='student_detail'),
#
#     url(r'^users/$', users_list, name='users_list'),
#     url(r'^users/(?P<pk>\d+)/$', user_detail, name='user_detail')
#
# ])













# from django.conf.urls import url
# from .views import views
# #格式后缀
# from rest_framework.urlpatterns import format_suffix_patterns
#
# urlpatterns = [
#     #GET /students
#     #POST /students/
#     url(r'^students/$',views.StudentsList.as_view()),  #as_view()的目的是让它作为视图来用
#     #GET /students/id
#     #PUT /students/id
#     #DELETE /students/id
#     url(r'^students/(?P<pk>\d+)/$', views.StudentDetail.as_view()),
#
#
#     url(r'^users/$',views.UserList.as_view()),
#     url(r'^user/(?P<pk>\d+)/$',views.UserDetail.as_view())
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)