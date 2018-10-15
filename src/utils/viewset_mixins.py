from abc import ABCMeta, abstractmethod
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ChangeOnlyViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet, metaclass=ABCMeta):
    """
    Returns base suite of mixins for View and Change REST methods and has abstract methods to return serializers
    to each action: list, get and update
    """
    http_method_names = ['get', 'patch']

    permission_classes = [IsAuthenticatedOrReadOnly,]

    @abstractmethod
    def get_serializer_class_for_list(self):
        pass

    @abstractmethod
    def get_serializer_class_for_detail(self):
        pass

    @abstractmethod
    def get_serializer_class_for_update(self):
        pass

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update'):
            return self.get_serializer_class_for_update()
        if self.action == 'list':
            return self.get_serializer_class_for_list()
        if self.action == 'retrieve':
            return self.get_serializer_class_for_detail()

        return self.serializer_class  # default value
