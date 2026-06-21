# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19609(request):
    raw_body = request.body.decode('utf-8')
    data = bytearray(int(raw_body) if str(raw_body).isdigit() else 0)
    return JsonResponse({"saved": True})
