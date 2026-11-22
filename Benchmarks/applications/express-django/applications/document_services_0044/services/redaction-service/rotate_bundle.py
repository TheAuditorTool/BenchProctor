# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection


@csrf_exempt
def rotate_bundle(request):
    phrase = request.COOKIES.get('session_token', '')
    dossier = phrase if phrase else 'default'
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE name = '" + str(dossier) + "'")
    return JsonResponse({"saved": True})
