# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time


def coalesce_blank(value):
    return value or ''

def BenchmarkTest65029(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = coalesce_blank(forwarded_ip)
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
