from knox.models import AuthToken
from knox.serializers import UserSerializer
from rest_framework import generics ,permissions
from rest_framework.response import Response
from auth_app.serilezer import *

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
class LoginAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            "suc":"شطور"
        })
class MainUser(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    def get_object(self):
      return self.request.user
