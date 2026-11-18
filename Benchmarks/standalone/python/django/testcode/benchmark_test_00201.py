# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00201(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    kind = 'json' if str(graphql_var).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(graphql_var).strip()
        case _:
            data = str(graphql_var)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
