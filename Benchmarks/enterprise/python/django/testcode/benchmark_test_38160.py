# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json
from types import SimpleNamespace


def BenchmarkTest38160(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
