from App.models import Student
from App.serializers import StudentSerializer
from rest_framework import mixins,generics

# class Index(APIView):
#     pass


#父类中有且只有一个能继承自APIView类 之所以使用generics.GenericAPIView目的就是为了能够让类继承APIView这个类，能够让这个类既是视图也是类;
class StudentsList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()  # 需得定义此属性，详情请见 mixins.ListModelMixin
    serializer_class = StudentSerializer  # 需的定义此属性，使用哪个类进行序列化对象

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

        # stus = Student.objects.all()
        # serializer = StudentSerializer(stus,many=True)
        # return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
        # serializer = StudentSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,status=status.HTTP_201_CREATED)
        # return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    # def getObject(self,pk):
    #     try:
    #         return Student.objects.get(pk=pk)
    #     except Student.DoesNotExist as e:
    #         raise Http404

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
        # stu = self.getObject(pk)
        # serializer = StudentSerializer(stu)
        # return Response(serializer.data)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
        # stu = self.getObject(pk)
        # serializer = StudentSerializer(stu, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,status=status.HTTP_201_CREATED)
        # return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
        # stu = self.getObject(pk)
        # stu.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)





# @api_view(['GET','POST'])
# def studentsList(request,format=None):
#     if request.method == 'GET':
#         stus = Student.objects.all()
#
#         serializer = StudentSerializer(stus,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET','PUT','DELETE'])
# def studentDetail(request,pk,format=None):
#     try:
#         stu = Student.objects.get(pk=pk)
#     except Student.DoesNotExist as e:
#         return Response({'error':str(e)},status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = StudentSerializer(stu)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
#
#
#     elif request.method == 'DELETE':
#         stu.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)