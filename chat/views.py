from django.contrib.auth.models import User
from django.db.models import Q
from django_filters import NumberFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import mixins
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from chat.models import Message
from chat.serializers import ChatUserSerializer, MessageSerializer


class UserViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ChatUserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = User.objects.exclude(id=self.request.user.id)
        return queryset

    def list(self, request, *args, **kwargs):
        """Allows authenticated users to list all users available for messaging."""
        return super().list(request, *args, **kwargs)


class UserFilter(NumberFilter):
    def filter(self, qs, value):
        return qs.filter(Q(sender_id=value) | Q(recipient_id=value)) if value else qs


class UserFilterSet(FilterSet):
    user = UserFilter(label="An user id to filter the messages.")

    class Meta:
        model = Message
        fields = ['user']


class MessageViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    serializer_class = MessageSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = UserFilterSet
    ordering = ['-timestamp']

    def get_queryset(self):
        queryset = Message.objects.filter(Q(sender=self.request.user) | Q(recipient=self.request.user))
        return queryset

    def list(self, request, *args, **kwargs):
        """Allows authenticated users to retrieve all of their messages, being able to filter by a specific user."""
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Allows authenticated users to send messages to another user by providing the recipient's identifier and content."""
        return super().create(request, *args, **kwargs)
