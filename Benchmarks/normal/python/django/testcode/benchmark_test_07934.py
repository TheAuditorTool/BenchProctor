# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


request_state: dict[str, str] = {}

def BenchmarkTest07934(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
