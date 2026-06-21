# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def ensure_str(value):
    return str(value)

def BenchmarkTest01605(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
