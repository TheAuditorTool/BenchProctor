# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


request_state: dict[str, str] = {}

def BenchmarkTest74319(request):
    cookie_value = request.COOKIES.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
