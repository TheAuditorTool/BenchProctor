# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27877(request):
    host_value = request.META.get('HTTP_HOST', '')
    prefix = ''
    data = prefix + str(host_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
