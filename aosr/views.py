from rest_framework import generics

from .models import ObjectActs
from .serializers import ObjectsActsSingleSerializer, ObjectActsListSerializer


class ObjectActsListView (generics.ListAPIView):
    serializer_class = ObjectActsListSerializer
    queryset = ObjectActs.objects.all()


class ObjectActsSingleView (generics.RetrieveAPIView):
    serializer_class = ObjectsActsSingleSerializer

    def get_queryset(self):
        return ObjectActs.objects.filter(id=self.kwargs['pk']).prefetch_related('aosr_set')
