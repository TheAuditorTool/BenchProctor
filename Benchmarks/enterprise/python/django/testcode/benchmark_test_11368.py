# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def BenchmarkTest11368(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
