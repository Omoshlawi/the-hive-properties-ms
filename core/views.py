from rest_framework import views
from rest_framework.response import Response
from rest_framework.reverse import reverse


class RootView(views.APIView):
    def get(self, request):
        return Response({
            "properties": reverse(viewname='properties:property-list', request=request),
            "groups": reverse(viewname='groups:group-list', request=request),
            "group_properties": reverse(viewname='groups:group-properties-list', request=request),
            "locations": reverse(viewname='properties:location-list', request=request),
        })
