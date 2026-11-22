# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection


@csrf_exempt
def prune_workspace(request):
    caption = request.COOKIES.get('session_token', '')
    synopsis = caption if caption else 'default'
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE name = '" + str(synopsis) + "'")
    return JsonResponse({"saved": True})
