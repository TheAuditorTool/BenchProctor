# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


def BenchmarkTest38010(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
