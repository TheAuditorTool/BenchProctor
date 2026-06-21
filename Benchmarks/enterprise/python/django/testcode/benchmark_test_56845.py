# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56845(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ' '.join(str(host_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
