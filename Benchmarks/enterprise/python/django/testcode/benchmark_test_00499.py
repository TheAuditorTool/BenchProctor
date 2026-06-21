# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00499(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
