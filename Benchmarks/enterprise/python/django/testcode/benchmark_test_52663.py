# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest52663(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    with open('/var/uploads/' + str(ua_value), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
