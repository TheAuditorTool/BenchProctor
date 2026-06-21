# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest15926(request):
    cookie_value = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
