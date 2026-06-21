# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest09923(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    pending = list(str(graphql_var).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
