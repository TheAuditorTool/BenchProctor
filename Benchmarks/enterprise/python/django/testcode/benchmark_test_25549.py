# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest25549(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    processed = data[:64]
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(processed)})
