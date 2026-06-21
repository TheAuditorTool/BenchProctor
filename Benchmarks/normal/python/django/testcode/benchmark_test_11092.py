# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import os
import time


request_state: dict[str, str] = {}

def BenchmarkTest11092(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        return redirect(str(data))
    return JsonResponse({"saved": True})
