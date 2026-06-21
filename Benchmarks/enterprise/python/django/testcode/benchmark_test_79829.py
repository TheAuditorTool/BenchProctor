# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest79829(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(graphql_var)})
