# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest09777(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
