# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22446(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
