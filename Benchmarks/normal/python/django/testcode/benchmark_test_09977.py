# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os
from types import SimpleNamespace


def BenchmarkTest09977(request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
