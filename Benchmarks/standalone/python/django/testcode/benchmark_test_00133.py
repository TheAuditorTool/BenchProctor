# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00133(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value!s}'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
