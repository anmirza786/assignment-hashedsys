
from django.http import Http404
from django.conf import settings
from rest_framework import status
from rest_framework import permissions
from .utils import get_tokens_for_user
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .serializer import CreateUserSerializer, UserSerializer

# get the user from the model
User = get_user_model()


class RegisterAPI(APIView):
    """REgister and login api instant """

    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)

        return Response({
            "user": CreateUserSerializer(user, context=self.get_serializer_context()).data,
            "Token": token

        })


class LoginAPI(APIView):
    """Login api instant """

    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({
                    'msg ': 'login success',
                    'name': user.name,
                    'email': user.email,
                    'id': user.id,
                    'is_active': user.is_active,
                    'is_staff': user.is_staff,
                    'token': get_tokens_for_user(user),

                })
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


class ForgetPasswordView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        if email is None:
            return Response({'error': 'Please provide an email address'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Email address not found'}, status=status.HTTP_404_NOT_FOUND)
        # send email
        send_mail(
            'Reset your password',
            'Follow this link to reset your password',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
