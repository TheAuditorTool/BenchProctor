# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest02537(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = default_blank(json_value)
    if data != request.session.get('csrf_token'):
        return JsonResponse({'error': 'CSRF token mismatch'}, status=403)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
