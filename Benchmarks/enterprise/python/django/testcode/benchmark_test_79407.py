# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest79407(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
