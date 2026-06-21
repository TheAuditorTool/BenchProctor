# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75228(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
