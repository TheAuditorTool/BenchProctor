# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest02216(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
