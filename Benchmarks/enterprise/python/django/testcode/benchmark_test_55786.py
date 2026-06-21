# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def relay_value(value):
    return value

def BenchmarkTest55786(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
