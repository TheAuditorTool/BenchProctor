# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def relay_value(value):
    return value

def BenchmarkTest70486(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
