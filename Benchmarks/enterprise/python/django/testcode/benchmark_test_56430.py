# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest56430(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if request.session.get('user') is None:
        return JsonResponse({'error': 'no session'}, status=401)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
