from App.models import Student
from App.serializers import StudentSerializer,UserSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from App.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



# #父类中有且只有一个能继承自APIView类
# class StudentsList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()  # 需得定义此属性，详情请见 mixins.ListModelMixin
#     serializer_class = StudentSerializer  # 需的定义此属性，使用哪个类进行序列化对象
#
#     #此permission的作用是：如果用户登录则执行以下post请求的代码，否则只能查看数据
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     #让用户在通过post请求创建一个新的student时，在保证创建学生的时会把request中的user赋值给该学生的owner字段
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     #只有所有者用户才能删除、修改，其他用户只能访问
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
#
#
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserDetail(generics.RetrieveDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer






