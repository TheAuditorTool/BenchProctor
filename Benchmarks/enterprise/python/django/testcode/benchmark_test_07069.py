# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import time


request_state: dict[str, str] = {}

def BenchmarkTest07069(request):
    cookie_value = request.COOKIES.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return JsonResponse({"saved": True})
