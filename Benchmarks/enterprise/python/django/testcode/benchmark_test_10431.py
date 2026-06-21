# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10431(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
