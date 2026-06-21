# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest02342(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = to_text(json_value)
    if data != request.session.get('csrf_token'):
        return JsonResponse({'error': 'CSRF token mismatch'}, status=403)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
