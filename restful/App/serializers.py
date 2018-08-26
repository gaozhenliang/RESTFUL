from rest_framework import serializers

from App.models import Student,Grade

'''
一个模型类对应一个序列化类
'''

#给学生创建序列化类
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id","name","sex","age","contend","isDelete","grade")   #将需要序列化的字段写到这个元组中


#给班级创建序列化类
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade

        fields = ("id","name","boyNum","girlNum","isDelete")