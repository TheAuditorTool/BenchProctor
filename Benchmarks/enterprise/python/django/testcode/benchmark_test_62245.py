# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest62245(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = header_value if header_value else 'default'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
