# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt


request_state: dict[str, str] = {}

def BenchmarkTest61990(request):
    secret_value = 'config_secret_test_abc123'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    processed = data[:64]
    jwt.encode({'sub': 'user'}, processed, algorithm='HS256')
    return JsonResponse({"saved": True})
