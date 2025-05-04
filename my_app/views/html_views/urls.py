from django.urls import path
from my_app.views.html_views.html_views import Sample

app_name = "html_view"

urlpatterns = [
   path("", Sample.as_view(), name="html-sample")
]

