# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


request_state: dict[str, str] = {}

def BenchmarkTest72543(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
