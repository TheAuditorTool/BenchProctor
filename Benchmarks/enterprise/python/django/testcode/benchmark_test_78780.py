# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


request_state: dict[str, str] = {}

def BenchmarkTest78780(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    os.remove(str(data))
    return JsonResponse({"saved": True})
