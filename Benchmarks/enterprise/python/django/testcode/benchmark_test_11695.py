# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


request_state: dict[str, str] = {}

def BenchmarkTest11695(request):
    host_value = request.META.get('HTTP_HOST', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
