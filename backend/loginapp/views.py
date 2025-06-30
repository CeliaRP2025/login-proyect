from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        # Ejemplo simple (aquí podrías usar autenticación real)
        if username == "admin" and password == "1234":
            return JsonResponse({"message": "Login exitoso"}, status=200)
        else:
            return JsonResponse({"message": "Credenciales inválidas"}, status=401)

    return JsonResponse({"error": "Método no permitido"}, status=405)
