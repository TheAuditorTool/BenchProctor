# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest47447(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
