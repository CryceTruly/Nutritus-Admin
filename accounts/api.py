from rest_framework import generics,permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer,RegisterSerializer,LoginSerializer
from django.contrib.auth.models import User

#registerapi
#login
#getuser

class RegistrationApi(generics.GenericAPIView):
    serializer_class=RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        newUser=User.objects.filter(email=request.data['email']).first()
        if newUser:
            return Response({"message":"Email is taken"},400)
        newUser2=User.objects.filter(username=request.data['username']).first()
        if newUser2:
            return Response({"message":"Username is taken"},400)
        password=request.data.get('password',None)
        if password is None:
            return Response({"message":"Password is required"},400)
        elif len(password)<6 and len(password)>16:

            return Response({"message":"Passwords should be between 6 to 16 character"},400)




        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)
        })

class LoginApi(generics.GenericAPIView):
    serializer_class=LoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)
        })



class UserApi(generics.RetrieveAPIView):
    permission_classes=[
        permissions.IsAuthenticated,
    ]

    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user