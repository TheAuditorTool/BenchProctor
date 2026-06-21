# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest71306(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
