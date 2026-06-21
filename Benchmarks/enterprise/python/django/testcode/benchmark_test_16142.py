# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16142(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = (lambda v: v.strip())(referer_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
