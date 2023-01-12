from django.urls import path
from app.views import Validator_Password


urlpatterns = [
    path('verify/', Validator_Password.as_view(), name='validator_password'),
]