# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection


@csrf_exempt
def summarize_record(request):
    synopsis = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    rendition = normalize(synopsis)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE name = '" + str(rendition) + "'")
    return JsonResponse({"saved": True})
