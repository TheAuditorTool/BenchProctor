# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


request_state: dict[str, str] = {}

def BenchmarkTest73757(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
