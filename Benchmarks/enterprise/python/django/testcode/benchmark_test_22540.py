# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time


request_state: dict[str, str] = {}

def BenchmarkTest22540(request):
    user_id = request.GET.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
