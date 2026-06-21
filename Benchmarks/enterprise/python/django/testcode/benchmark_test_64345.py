# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest64345(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
