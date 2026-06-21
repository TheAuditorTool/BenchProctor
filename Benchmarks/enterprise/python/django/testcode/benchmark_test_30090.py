# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest30090(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
