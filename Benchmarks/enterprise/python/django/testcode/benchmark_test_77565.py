# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77565(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
