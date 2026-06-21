# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def coalesce_blank(value):
    return value or ''

def BenchmarkTest69289(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = coalesce_blank(forwarded_ip)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
