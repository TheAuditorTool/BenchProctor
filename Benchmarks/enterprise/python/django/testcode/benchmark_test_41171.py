# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json
from types import SimpleNamespace


def BenchmarkTest41171(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
