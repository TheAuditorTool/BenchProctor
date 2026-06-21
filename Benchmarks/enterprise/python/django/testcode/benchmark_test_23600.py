# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def to_text(value):
    return str(value).strip()

def BenchmarkTest23600(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
