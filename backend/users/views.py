from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()
print("Users----------", User.objects.all())
# Create your views here.
class RegistrationView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the user and get the instance
            username = user.username  # Assuming 'username' is the field name
            return Response({"message": f"user account for {username} created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
