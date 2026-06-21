# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def BenchmarkTest71806(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
