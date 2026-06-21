# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62693(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = auth_header if auth_header else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
