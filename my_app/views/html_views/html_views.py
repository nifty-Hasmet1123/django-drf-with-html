from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class Sample(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "my_app/index.html"
    
    def get(self, request):
        form = AuthenticationForm()
        return Response({"form": form})
        