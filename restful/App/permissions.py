from rest_framework import permissions
from django.contrib.auth import login

#自定义的一个权限，用于让其当前用户只能操作当前用户的数据，所有用户只能获取数据
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #如果当前用户的请求不是GET的话，则得继续去判断是否是当前用户在操作自己的数据
        if request.method in permissions.SAFE_METHODS:
            return True
        #代表的是当前学生对象。如果操作的那个学生对象的owner用户跟当前登录的用户相等，则说明是当前用户在操作当前用户的数据，返回True 否则返回False，
        return  obj.owner == request.user