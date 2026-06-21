# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest42512(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    try:
        processed = int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'forbidden'}, status=400)
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return JsonResponse({"saved": True})
