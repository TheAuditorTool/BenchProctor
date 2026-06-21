# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest00112(request):
    host_value = request.META.get('HTTP_HOST', '')
    pending = list(str(host_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
