from rest_framework import viewsets
from .models import Person
from .serializers import PersonReadSerializer, PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.select_related("team").all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PersonReadSerializer
        return PersonSerializer
