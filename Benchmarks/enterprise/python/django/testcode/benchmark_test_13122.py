# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest13122(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
