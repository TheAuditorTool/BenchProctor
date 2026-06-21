# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest67357(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = coalesce_blank(json_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
