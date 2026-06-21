# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest53655(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
