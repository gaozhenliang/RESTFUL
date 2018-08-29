from django.contrib.auth.models import User
from App.models import Student,Grade


from App.serializers import StudentSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response





@api_view(['GET','POST'])
def studentsList(request,format=None):
    if request.method == 'GET':
        stus = Student.objects.all()

        serializer = StudentSerializer(stus,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def studentDetail(request,pk,format=None):
    try:
        stu = Student.objects.get(pk=pk)
    except Student.DoesNotExist as e:
        return Response({'error':str(e)},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(stu)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)