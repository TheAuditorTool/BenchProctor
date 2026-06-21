# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest76032(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
