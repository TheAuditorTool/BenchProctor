# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest12215(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    db.execute('SELECT * FROM users ORDER BY ' + str(processed))
    return JsonResponse({"saved": True})
