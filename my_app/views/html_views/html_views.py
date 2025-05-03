from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from my_app.models import Owner

# Create your views here.
class SummaryHTMLView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'my_app/index.html'

    def get(self, request):
        owners = Owner.objects.all()
        return Response({'owners': owners})