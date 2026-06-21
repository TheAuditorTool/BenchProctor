# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json


def BenchmarkTest14707(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
