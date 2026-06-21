# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest06961(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
