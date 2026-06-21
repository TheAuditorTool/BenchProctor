# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00416(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '{}'.format(auth_header)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
