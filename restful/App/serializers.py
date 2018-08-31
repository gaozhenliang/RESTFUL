from rest_framework import serializers

from App.models import Student,Grade

'''
一个模型类对应一个序列化类
'''

#给学生创建序列化类
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')   #序列化的时候展示学生所属用户
        model = Student
        fields = ("id","name","sex","age","contend","isDelete","grade","owner")   #将需要序列化的字段写到这个元组中


#给班级创建序列化类
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade

        fields = ("id","name","boyNum","girlNum","isDelete")


from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "students")


