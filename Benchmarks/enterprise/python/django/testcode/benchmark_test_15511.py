# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest15511(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
