# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def coalesce_blank(value):
    return value or ''

def BenchmarkTest62197(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = coalesce_blank(ua_value)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
