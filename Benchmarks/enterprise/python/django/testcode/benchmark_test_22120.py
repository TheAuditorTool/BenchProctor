# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest22120(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
