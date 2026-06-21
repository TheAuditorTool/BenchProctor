# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest44295(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    if data != request.session.get('csrf_token'):
        return JsonResponse({'error': 'CSRF token mismatch'}, status=403)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
