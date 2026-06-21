# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25111(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
