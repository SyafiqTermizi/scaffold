from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import User


class UserCreationSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    password_2 = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )

    class Meta:
        model = User
        fields = ("username", "email", "password_1", "password_2")

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                detail="User with given username already exist",
                code="user_exist",
            )
        return username

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                detail="User with given username already exist",
                code="user_exist",
            )
        return email

    def validate(self, attrs):
        validated_data = super().validate(attrs)

        if validated_data["password_1"] != validated_data["password_2"]:
            raise serializers.ValidationError(
                detail="Password Not Match",
                code="password_mismatch",
            )
        validate_password(validated_data["password_1"])
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password_1"],
        )
