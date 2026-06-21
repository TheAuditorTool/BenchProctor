# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def BenchmarkTest16911(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
