# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31270(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = (lambda v: v.strip())(forwarded_ip)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
