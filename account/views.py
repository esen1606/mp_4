from django.contrib.auth import get_user_model, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistrationSerializer, ActivationSerializer, UserSerializer,  ConfirmPasswordSerializer, ResetPasswordSerializer
from rest_framework.generics import GenericAPIView, get_object_or_404, ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from django.views import View
from account.models import CustomUser
from rest_framework import status
from django.urls import reverse
User = get_user_model()
from django.shortcuts import get_list_or_404
from project.tasks import send_confirmation_email_task, send_confirmation_password_task
from .send_email import send_confirmation_email, send_confirmation_password
from drf_yasg.utils import swagger_auto_schema

class RegistrationView(APIView):
    @swagger_auto_schema(request_body=RegistrationSerializer)
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_confirmation_email(email=user.email, code=user.activation_code)
                # send_confirmation_email_task.delay(email=user.email, code=user.activation_code)
            except:
                return Response({'message': "Зарегистрировался но на почту код не отправился",
                                 'data': serializer.data}, status=201)
        return Response(serializer.data, status=201)


class ActivationView(GenericAPIView):
    serializer_class = ActivationSerializer

    def get(self, request):
        code = request.GET.get('u')
        users = get_list_or_404(User, activation_code=code)
        for user in users:
            user.is_active = True
            user.activation_code = ''
            user.save()
        return Response('Успешно активирован', status=200)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Успешно активирован', status=200)



class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=200)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=400)

class DashboardView(View):
    template_name = 'account/dashboard.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        action = request.POST.get('action', None)

        if action == 'login':
            return redirect('login')
        elif action == 'register':
            return redirect('registration')
        else:
            return render(request, self.template_name, {'error': 'Invalid action'})

def activation_view(request):
    return render(request, 'account/activation.html')

class ResetPasswordView(APIView):
    def get(self, request):
        return Response({'message': 'Please provide an email to reset the password'})

    @swagger_auto_schema(request_body=ConfirmPasswordSerializer)
    def post(self, request):
        serializer = ConfirmPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                send_confirmation_password(user.email, user.activation_code)
                # send_confirmation_password_task.delay(user.email, user.activation_code)
                return Response({'activation_code': user.activation_code}, status=200)
            except User.DoesNotExist:
                return Response({'message': 'User with this email does not exist.'}, status=404)
        return Response(serializer.errors, status=400)


class ResetPasswordConfirmView(APIView):
    @swagger_auto_schema(request_body=ResetPasswordSerializer)
    def post(self, request):
        code = request.GET.get('u')
        user = get_object_or_404(User, activation_code=code)
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_password = serializer.validated_data['new_password']
        user.set_password(new_password)
        user.activation_code = ''
        user.save()
        return Response('Your password has been successfully updated', status=200)




