# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection


@csrf_exempt
def collect_bundle(request):
    memo = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    verdict = normalize(memo)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE name = '" + str(verdict) + "'")
    return JsonResponse({"saved": True})
