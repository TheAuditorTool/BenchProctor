# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection


@csrf_exempt
def build_invoice(request):
    footnote = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    remittance = normalize(footnote)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE name = '" + str(remittance) + "'")
    return JsonResponse({"saved": True})
