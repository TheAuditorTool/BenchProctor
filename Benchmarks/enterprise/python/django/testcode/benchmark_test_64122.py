# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest64122(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
