# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00504(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return JsonResponse({"saved": True})
