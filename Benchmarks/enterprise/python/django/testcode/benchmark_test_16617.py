# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16617(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(auth_header))
    return JsonResponse({"saved": True})
