# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time


def ensure_str(value):
    return str(value)

def BenchmarkTest68877(request):
    user_id = request.GET.get('id', '')
    data = ensure_str(user_id)
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return JsonResponse({"saved": True})
