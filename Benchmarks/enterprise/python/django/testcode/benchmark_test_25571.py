# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest25571(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = default_blank(json_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
