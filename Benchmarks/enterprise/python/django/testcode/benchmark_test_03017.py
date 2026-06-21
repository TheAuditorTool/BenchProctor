# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest03017(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    auth_check('user', data)
    return JsonResponse({"saved": True})
