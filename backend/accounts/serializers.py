from rest_framework import serializers
from .models import LabTechUser
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from rest_framework.settings import api_settings

# Use your custom user model here
class LabTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTechUser
        fields = ('id', 'username', 'department','is_labtech')
        read_only_fields = ('username')

        extra_kwargs = {
            'password': {'write_only': True},
        }

class LabTechRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password', 'placeholder': 'Password'})
    
    class Meta:
        model = LabTechUser    
        fields = ('username', 'email', 'password','department','is_labtech',
                  'first_name', 'last_name')

    def validate(self, attrs):
        user = self.Meta.model(**attrs)
        password = attrs.get("password")
        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error[api_settings.NON_FIELD_ERRORS_KEY]}
            )

        return super().validate(attrs)
