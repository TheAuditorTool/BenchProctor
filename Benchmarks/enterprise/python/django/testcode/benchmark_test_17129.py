# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17129(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
