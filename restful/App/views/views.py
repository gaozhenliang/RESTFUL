from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from App.models import Student,Grade

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.utils.six import BytesIO

from App.serializers import StudentSerializer,GradeSerializer

# Create your views here.




def studentsList(request):
    if request.method == 'GET':
        stus = Student.objects.all()   #得到一个对象列表
        #序列化对象
        #将对象列表转换为一个json字符串
        serializer = StudentSerializer(stus,many=True)  #many为True时，序列化列表中所有元素
        return JsonResponse(serializer.data,safe=False)   #safe为False时，表示不安全
    elif request.method == 'POST':
        #接收客户端传递过来的数据
        # print('request.POST is {}'.format(request.POST))   #<QueryDict: {'grade': ['1'], 'name': ['高亮'], 'contend': ['da shuai bi'], 'age': ['24'],
        content = JSONRenderer().render(request.POST)  #渲染成json格式的数据
        # print('content is {}'.format(content))   #b'{"grade":"1","name":"\xe9\xab\x98\xe4\xba\xae","contend":"da shuai bi","age":"24","sex":"1","owner":"1"}'
        stream = BytesIO(content)     #对字节流的数据解析成bytesio对象
        # print('stream is {}'.format(stream))   #<_io.BytesIO object at 0x7fb8d61afeb8>
        stuDict = JSONParser().parse(stream)   #解析bytesio对象
        # print('stuDict is {}'.format(stuDict))  #{'grade': '1', 'name': '高亮', 'contend': 'da shuai bi', 'age': '24', 'sex': '1', 'owner': '1'}
        serializer = StudentSerializer(data=stuDict)  #序列化成一个对象
        # print('serializer is {}'.format(serializer)) #  StudentSerializer(data={'grade': '1', 'name': '高亮', 'contend': 'da shuai bi', 'age': '24''sex': '1', 'owner': '1'}):

        if serializer.is_valid():
            #存数据
            serializer.save()  #返回一个添加完成后的对象
            return JsonResponse(serializer.data,status=201)
        return JsonResponse({'error':serializer.errors},status=400)


def studentDetail(request,pk):
    try:
        stu = Student.objects.get(pk=pk)
    except Student.DoesNotExist as e:
        return JsonResponse({'error':str(e)},status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(stu)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        print('stu is {}'.format(stu))
        print('request.POST is {}'.format(request.POST))
        content = JSONRenderer().render(request.POST)
        stream = BytesIO(content)
        stuDict = JSONParser().parse(stream)
        #修改
        #如果不带stu这个原对象，则为创建，如果带上原对象，则为修改
        serializer = StudentSerializer(stu,data=stuDict)  #把后面的数据对前面的数据进行替换
        if serializer.is_valid():
            #存数据
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse({'error':serializer.errors},status=400)
    elif request.method == 'DELETE':
        stu.delete()
        return HttpResponse(status=204,content_type='application/json')