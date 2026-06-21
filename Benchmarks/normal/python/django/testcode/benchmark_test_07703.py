# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest07703(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
