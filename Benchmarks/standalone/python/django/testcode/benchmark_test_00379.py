# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00379(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(auth_header).split(',')
    data = ' '.join(parts)
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return JsonResponse({"saved": True})
