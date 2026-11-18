# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00004(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
