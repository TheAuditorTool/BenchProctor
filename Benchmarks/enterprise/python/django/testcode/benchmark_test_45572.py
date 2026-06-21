# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest45572(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    auth_check('user', processed)
    return JsonResponse({"saved": True})
