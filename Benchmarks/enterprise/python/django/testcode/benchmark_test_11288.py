# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest11288(request):
    raw_body = request.body.decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
