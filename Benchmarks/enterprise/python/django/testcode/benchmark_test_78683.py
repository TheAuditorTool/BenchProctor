# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78683(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
