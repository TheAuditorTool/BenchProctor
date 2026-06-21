# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest22835(request):
    host_value = request.META.get('HTTP_HOST', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return JsonResponse({"saved": True})
