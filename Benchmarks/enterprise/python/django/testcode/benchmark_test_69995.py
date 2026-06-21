# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest69995(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if json_value != request.session.get('csrf_token'):
        return JsonResponse({'error': 'CSRF token mismatch'}, status=403)
    db.execute('UPDATE users SET name = ?', (str(json_value),))
    return JsonResponse({"saved": True})
