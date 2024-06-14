from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'role', 'password', "password2")
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }

    
    # Validates if password and confirm password tallies
    def validate(self, data):
        if (data['password'] != data['password2']):
            raise serializers.ValidationError("Passwords do not match!")
        return data
    
    def create(self, validated_data):
       validated_data.pop("password2") #removes password2
       user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role = validated_data['role']
        )
       user.set_password(validated_data['password']) #hashes password before saving it
       user.save()
       return user