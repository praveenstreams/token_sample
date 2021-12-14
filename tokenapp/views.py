from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import userserializer,userregisterserializer,alldata,deletedata
from django.http import HttpResponse
from rest_framework.views import APIView



class registerapi(generics.GenericAPIView):
    serializer_class = userregisterserializer

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid()
        user=serializer.save()

        return Response({
            "user":userserializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })

from django.contrib.auth import login
from knox.views import LoginView as klv
from rest_framework.authtoken.serializers import AuthTokenSerializer
# class loginapi(klv):
#     permission_classes = (permissions.AllowAny)
#
#     def post(self, request, format=None):
#         serializer=AuthTokenSerializer(data=request.data)
#         serializer.is_valid()
#         user=serializer.validated_data['user']
#
#         login(request,user)
#
#         return super(loginapi,self).post(request,format=None)


class loginapi(klv):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self,request,*args,**kwargs):
        d=request.data
        serializer = AuthTokenSerializer(data=d)
        if serializer.is_valid():
        #     return user=serializer.validated_data['user']
        # login(request, user)
            return HttpResponse("Valid User")
        else:
            return HttpResponse("Not valid user")
from django.contrib.auth.models import User


class deleteview(APIView):


    def get(self,request,*args,**kwargs):
        qs=User.objects.all()
        serializer=alldata(qs,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        d=request.data
        serializer=deletedata(data=d)
        serializer.is_valid()
        User.objects.get(id=d['id']).delete()
        return Response(serializer.errors)







