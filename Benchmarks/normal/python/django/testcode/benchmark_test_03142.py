# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest03142(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = relay_value(ua_value)
    processed = data[:64]
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return JsonResponse({"saved": True})
