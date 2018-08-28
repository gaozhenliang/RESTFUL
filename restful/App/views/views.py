from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from App.models import Student,Grade

# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from django.utils.six import BytesIO

from App.serializers import StudentSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response





@api_view(['GET','POST'])
def studentsList(request):
    if request.method == 'GET':
        stus = Student.objects.all()

        serializer = StudentSerializer(stus,many=True)
        #不需要制定json格式，返回客户端可以返回json或者HTML，返回HTML内容的话，会在浏览器中经过渲染成页面
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # content = JSONRenderer().render(request.POST)
        # stream = BytesIO(content)
        # stuDict = JSONParser().parse(stream)
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def studentDetail(request,pk):
    try:
        stu = Student.objects.get(pk=pk)
    except Student.DoesNotExist as e:
        return Response({'error':str(e)},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(stu)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # content = JSONRenderer().render(request.POST)
        # stream = BytesIO(content)
        # stuDict = JSONParser().parse(stream)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            #存数据
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)