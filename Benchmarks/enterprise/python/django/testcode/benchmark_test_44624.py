# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44624(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
