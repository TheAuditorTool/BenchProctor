# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


request_state: dict[str, str] = {}

def BenchmarkTest65621(request):
    raw_body = request.body.decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
