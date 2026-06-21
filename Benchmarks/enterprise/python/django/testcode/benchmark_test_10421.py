# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest10421(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
