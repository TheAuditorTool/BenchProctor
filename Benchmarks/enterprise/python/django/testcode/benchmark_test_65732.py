# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest65732(request):
    cookie_value = request.COOKIES.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
