# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest73410(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
