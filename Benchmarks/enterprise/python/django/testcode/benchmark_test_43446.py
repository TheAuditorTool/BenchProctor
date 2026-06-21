# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


request_state: dict[str, str] = {}

def BenchmarkTest43446(request):
    cookie_value = request.COOKIES.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    if str(processed) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
