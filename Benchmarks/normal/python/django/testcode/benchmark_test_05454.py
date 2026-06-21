# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


request_state: dict[str, str] = {}

def BenchmarkTest05454(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
