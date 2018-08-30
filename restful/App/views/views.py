from App.models import Student
from App.serializers import StudentSerializer
from rest_framework import generics

#父类中有且只有一个能继承自APIView类
class StudentsList(generics.ListCreateAPIView):
    queryset = Student.objects.all()  # 需得定义此属性，详情请见 mixins.ListModelMixin
    serializer_class = StudentSerializer  # 需的定义此属性，使用哪个类进行序列化对象


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer







