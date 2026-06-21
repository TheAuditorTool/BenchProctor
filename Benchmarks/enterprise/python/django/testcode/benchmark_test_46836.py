# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest46836(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
