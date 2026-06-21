# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json
import os
from types import SimpleNamespace


def BenchmarkTest00763(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
