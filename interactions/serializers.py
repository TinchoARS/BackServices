from rest_framework import serializers
from .models import Posts, Requests, StatusServices
from users.serializers import UsersSerializer
from services.serializers import ServicesSerializer
from services.models import Services
from django.utils import timezone
from rest_framework.exceptions import ValidationError


class PostsSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)

    class Meta:
        model = Posts
        fields = '__all__'
        extra_kwargs = {
            # Hacer que el campo user sea de solo lectura
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        # Extraer el usuario autenticado del contexto
        user = self.context['request'].user
        if not user.is_supplier:
            raise serializers.ValidationError(
                "Only suppliers can create posts.")
        post = Posts.objects.create(user=user, **validated_data)
        return post


class RequestsSerializer(serializers.ModelSerializer):
    # ya que no pasamos el post solo queremos ver sus datos
    post = PostsSerializer(read_only=True)

    class Meta:
        model = Requests
        fields = ['message', 'status', 'reason', 'post_id', 'user_id', 'post']
        extra_kwargs = {'reason': {'required': False}}

    def create(self, validated_data):

        # Extraer los campos adicionales del contexto
        user = self.context['request'].user
        if not user.is_finder:
            raise serializers.ValidationError(
                "Only search engines can create requests.")

        post_id = self.context['request'].data.get('post_id')
        post = Posts.objects.get(id=post_id)
        if not post_id:
            raise serializers.ValidationError("post_id is required.")
        validated_data['post_id'] = post_id

        request = Requests.objects.create(post=post,
                                          **validated_data)  # Crear la solicitud
        return request

    def update(self, instance, validated_data):
        status = validated_data.get('status', instance.status)
        reason = validated_data.get('reason', instance.reason)
        if status == 'rejected' and not reason:
            raise serializers.ValidationError(
                "The reason is required when the status is 'rejected'.")
        instance.status = status
        instance.reason = reason
        instance.save()
        if status == 'accepted':
            StatusServices.objects.create(request=instance, status='accepted',
                                          comment='The search engine has accepted the request.', user=instance.user)
        return instance


class StatusServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusServices
        fields = '__all__'

    def create(self, validated_data):
        status_service = StatusServices.objects.create(**validated_data)
        return status_service

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.dateupdated = timezone.now()
        instance.save()
        return instance
