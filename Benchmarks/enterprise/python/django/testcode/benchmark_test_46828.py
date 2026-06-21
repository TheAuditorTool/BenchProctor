# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


request_state: dict[str, str] = {}

def BenchmarkTest46828(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
