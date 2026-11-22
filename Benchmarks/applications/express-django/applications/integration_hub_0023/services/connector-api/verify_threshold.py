# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection


@csrf_exempt
def verify_threshold(request):
    caption = request.COOKIES.get('session_token', '')
    handshake = caption if caption else 'default'
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE name = '" + str(handshake) + "'")
    return JsonResponse({"saved": True})
