# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest56225(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
