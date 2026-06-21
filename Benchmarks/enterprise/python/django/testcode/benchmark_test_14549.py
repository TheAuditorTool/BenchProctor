# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


request_state: dict[str, str] = {}

def BenchmarkTest14549(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
