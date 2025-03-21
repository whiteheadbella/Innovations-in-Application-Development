from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Chatbot UI view
def chatbot_views(request):
    return render(request, 'chatbot/chatbot.html')  # Match template path!

# Dialogflow Webhook
@csrf_exempt
def dialogflow_webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        intent = data['queryResult']['intent']['displayName']

        # Respond based on intent
        if intent == 'how_are_you_feeling':
            response_text = "I'm doing great, thank you for asking! 😊"

        elif intent == 'book_flight':
            response_text = "Sure! Where would you like to fly?"

        elif intent == 'order_food':
            response_text = "Yum! What would you like to order today?"

        elif intent == 'view_employee':
            response_text = "Here are a few employees: John, Sara, and Ali."

        else:
            response_text = "I'm not sure how to help with that yet."

        return JsonResponse({"fulfillmentText": response_text})

    return JsonResponse({"error": "Only POST requests are accepted."})

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("User message:", data)
            user_message = data.get("message", "")
            bot_response = f"You said: {user_message}"
            return JsonResponse({"response": bot_response})
        except Exception as e:
            print("Error:", e)
            return JsonResponse({"response": "Oops, something went wrong."}, status=500)
