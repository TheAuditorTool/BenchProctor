# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest60368(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
