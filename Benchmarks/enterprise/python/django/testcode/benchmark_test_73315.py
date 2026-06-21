# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time


def coalesce_blank(value):
    return value or ''

def BenchmarkTest73315(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = coalesce_blank(auth_header)
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return JsonResponse({"saved": True})
