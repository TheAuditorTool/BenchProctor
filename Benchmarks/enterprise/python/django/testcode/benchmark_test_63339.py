# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json


def ensure_str(value):
    return str(value)

def BenchmarkTest63339(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
