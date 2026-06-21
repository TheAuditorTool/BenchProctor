# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55356(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
