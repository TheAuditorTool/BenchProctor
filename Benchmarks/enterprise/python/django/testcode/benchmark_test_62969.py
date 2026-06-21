# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62969(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(referer_value))
    return JsonResponse({"saved": True})
