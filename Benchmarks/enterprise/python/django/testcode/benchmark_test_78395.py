# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


request_state: dict[str, str] = {}

def BenchmarkTest78395(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
