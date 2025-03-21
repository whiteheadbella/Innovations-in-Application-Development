from django.urls import path
from .views import chatbot_views, dialogflow_webhook

urlpatterns = [
    path('dialogflow-webhook/', dialogflow_webhook, name='dialogflow_webhook'),
    path('chatbot/', chatbot_views, name='chatbot_views'),  # For chatbot page
]
