# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from types import SimpleNamespace


def BenchmarkTest58892(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
