# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from types import SimpleNamespace


def BenchmarkTest18800(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
