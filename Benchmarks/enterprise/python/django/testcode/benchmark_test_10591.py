# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import time


request_state: dict[str, str] = {}

def BenchmarkTest10591(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
    return JsonResponse({"saved": True})
