# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73391(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
