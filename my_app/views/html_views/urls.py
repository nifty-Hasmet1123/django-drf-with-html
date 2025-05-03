from django.urls import path
from my_app.views import SummaryHTMLView

app_name = "html_view"

urlpatterns = [
    path("", SummaryHTMLView.as_view(), name="owner-api")
]

