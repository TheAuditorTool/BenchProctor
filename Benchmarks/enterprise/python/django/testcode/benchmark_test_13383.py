# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13383(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
