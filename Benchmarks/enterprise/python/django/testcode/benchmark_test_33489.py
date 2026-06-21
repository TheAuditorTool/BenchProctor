# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33489(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(ua_value))
    return JsonResponse({"saved": True})
