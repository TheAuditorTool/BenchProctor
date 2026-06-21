# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14712(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
