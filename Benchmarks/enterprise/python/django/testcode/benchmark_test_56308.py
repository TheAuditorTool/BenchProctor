# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56308(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
