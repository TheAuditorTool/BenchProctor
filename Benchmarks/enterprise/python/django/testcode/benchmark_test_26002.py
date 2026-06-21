# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time


request_state: dict[str, str] = {}

def BenchmarkTest26002(request):
    cookie_value = request.COOKIES.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        eval(str(data))
    return JsonResponse({"saved": True})
