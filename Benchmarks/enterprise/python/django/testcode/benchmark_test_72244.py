# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72244(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
