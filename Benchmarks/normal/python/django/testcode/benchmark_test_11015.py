# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from types import SimpleNamespace


def BenchmarkTest11015(request):
    raw_body = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
