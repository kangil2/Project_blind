from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status

from .serializers import SignUpSerializer

class SignUpView(APIView):
    @swagger_auto_schema(request_body=SignUpSerializer,responses={200: SignUpSerializer})
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user          = serializer.save()
            token         = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token  = str(token.access_token)
            response           = Response({
                "user"    : serializer.data,
                "message" : "successs",
                "token"   : {
                    "access"  : access_token,
                    "refresh" : refresh_token
                }},
                status = status.HTTP_200_OK,
            )
            response.set_cookie("access", access_token, httponly=True)
            response.set_cookie("refresh", refresh_token, httponly=True)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)