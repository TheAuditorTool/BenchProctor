# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest61008(request):
    cookie_value = request.COOKIES.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if request.session.get('role') != 'admin':
        return JsonResponse({'error': 'forbidden'}, status=403)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
