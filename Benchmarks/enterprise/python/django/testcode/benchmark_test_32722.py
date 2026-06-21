# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def BenchmarkTest32722(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
