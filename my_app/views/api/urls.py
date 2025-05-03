from django.urls import path
from my_app.views import OwnerSummaryAPI

app_name = "api_view"

urlpatterns = [
    path("summary", OwnerSummaryAPI.as_view(), name="owner-api")
]

