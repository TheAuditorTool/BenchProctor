# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30913(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
