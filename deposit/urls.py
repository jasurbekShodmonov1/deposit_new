from django.urls import path, include
from .views import predict_fraud

urlpatterns = [
    path("", predict_fraud, name="predict_fraud"),

]