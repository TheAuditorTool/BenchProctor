# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os
from types import SimpleNamespace


def BenchmarkTest55613(request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
