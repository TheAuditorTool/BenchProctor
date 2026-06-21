# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest74766(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
