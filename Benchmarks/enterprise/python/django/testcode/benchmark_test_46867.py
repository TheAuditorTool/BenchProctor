# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46867(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
