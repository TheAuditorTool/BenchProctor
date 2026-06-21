# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest30202(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
