# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest53456(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    if data != request.session.get('csrf_token'):
        return JsonResponse({'error': 'CSRF token mismatch'}, status=403)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
