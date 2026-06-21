# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60266(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
