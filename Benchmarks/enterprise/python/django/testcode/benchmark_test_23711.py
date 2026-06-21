# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23711(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(auth_header))
    return JsonResponse({"saved": True})
