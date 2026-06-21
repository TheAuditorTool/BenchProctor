# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest50112(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
