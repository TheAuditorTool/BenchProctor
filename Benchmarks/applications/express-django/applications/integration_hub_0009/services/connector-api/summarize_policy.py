# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection


@csrf_exempt
def summarize_policy(request):
    heading = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(heading)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE name = '" + str(handshake) + "'")
    return JsonResponse({"saved": True})
