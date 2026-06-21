# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest72083(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    if not re.fullmatch('^[\\w\\s.\\-:/=\\r\\n]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
