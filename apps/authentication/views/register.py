from rest_framework import generics
from rest_framework.response import Response

from ..serializers import RegisterSerializer, UserSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        serialized_data = UserSerializer(
            user, context=self.get_serializer_context()).data
        return Response({
            "user": serialized_data,
            "message": "User Created Successfully. Now perform Login to get your token",
        })
