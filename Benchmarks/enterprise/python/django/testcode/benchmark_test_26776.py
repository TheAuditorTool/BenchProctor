# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest26776(request):
    host_value = request.META.get('HTTP_HOST', '')
    with open('/var/uploads/' + str(host_value), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
