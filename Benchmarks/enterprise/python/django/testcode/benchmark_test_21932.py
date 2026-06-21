# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21932(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
