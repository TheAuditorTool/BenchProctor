# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


request_state: dict[str, str] = {}

def BenchmarkTest79946(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
