# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def to_text(value):
    return str(value).strip()

def BenchmarkTest10904(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = to_text(json_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
