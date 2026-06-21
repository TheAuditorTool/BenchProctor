# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76560(request):
    raw_body = request.body.decode('utf-8')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(raw_body))
    return JsonResponse({"saved": True})
