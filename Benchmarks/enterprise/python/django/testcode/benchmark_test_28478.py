# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json
from types import SimpleNamespace


def BenchmarkTest28478(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
