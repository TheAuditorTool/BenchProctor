# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest34901(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return JsonResponse({"saved": True})
