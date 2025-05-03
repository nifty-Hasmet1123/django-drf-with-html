from rest_framework.views import APIView
from rest_framework.response import Response
from my_app.serializers import OwnerSerializer
from my_app.models import Owner

# rest api here
class OwnerSummaryAPI(APIView):
    def get(self, request):
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        
        return Response(serializer.data)
