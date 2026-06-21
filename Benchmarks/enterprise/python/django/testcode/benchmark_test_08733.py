# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest08733(request):
    user_id = request.GET.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    try:
        processed = int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'forbidden'}, status=400)
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return JsonResponse({"saved": True})
