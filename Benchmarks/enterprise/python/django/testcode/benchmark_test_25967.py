# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from types import SimpleNamespace


def BenchmarkTest25967(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
