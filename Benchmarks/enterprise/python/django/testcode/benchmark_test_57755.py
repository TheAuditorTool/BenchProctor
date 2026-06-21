# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57755(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
