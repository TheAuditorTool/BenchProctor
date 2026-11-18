# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00256(request):
    host_value = request.META.get('HTTP_HOST', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
