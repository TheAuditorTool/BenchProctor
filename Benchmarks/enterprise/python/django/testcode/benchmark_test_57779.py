# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57779(request):
    raw_body = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
