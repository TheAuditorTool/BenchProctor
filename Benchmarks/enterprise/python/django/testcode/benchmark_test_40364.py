# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from types import SimpleNamespace


def BenchmarkTest40364(request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
