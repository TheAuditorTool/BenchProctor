# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57928(request):
    raw_body = request.body.decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
