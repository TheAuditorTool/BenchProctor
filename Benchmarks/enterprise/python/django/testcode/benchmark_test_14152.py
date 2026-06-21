# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def BenchmarkTest14152(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
