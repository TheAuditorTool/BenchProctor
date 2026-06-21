# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest80936(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    try:
        processed = int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'forbidden'}, status=400)
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return JsonResponse({"saved": True})
