# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28606(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(forwarded_ip))
    return JsonResponse({"saved": True})
