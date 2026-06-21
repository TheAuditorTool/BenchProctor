# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest21868(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
