from django.db import models

# Create your models here.

class Grade(models.Model):
    name = models.CharField(max_length=20)
    boyNum = models.IntegerField()
    girlNum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'grades'

    def __str__(self):
        return self.name



class StudentManager(models.Manager):
     def get_queryset(self):
         return super(StudentManager,self).get_queryset().filter(isDelete=False)


class Student(models.Model):
    objects = StudentManager()

    name = models.CharField(max_length=20)
    sex = models.BooleanField()
    age = models.IntegerField()
    contend = models.CharField(max_length=40)

    grade = models.ForeignKey(Grade)
    isDelete = models.BooleanField(default=False)

    owner = models.ForeignKey('auth.User',related_name='students')  #给user类添加了一个字段students，这样做的话就能查看当前用户下的学生 相当与request.user.student_set（）

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'students'

    @classmethod
    def create(cls,name,sex,age,contend,grade):
        return cls(name=name,sex=sex,age=age,contend=contend,grade=grade)