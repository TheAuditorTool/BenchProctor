# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24394(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
