# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05618(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value:.200s}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
