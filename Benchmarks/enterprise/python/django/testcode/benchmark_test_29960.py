# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest29960(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
