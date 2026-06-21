# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest46643(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = (lambda v: v.strip())(forwarded_ip)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
