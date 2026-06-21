# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from types import SimpleNamespace


def BenchmarkTest62497(request):
    user_id = request.GET.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
