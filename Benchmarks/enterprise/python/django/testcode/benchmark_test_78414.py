# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78414(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
