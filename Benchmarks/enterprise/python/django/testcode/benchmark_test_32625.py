# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32625(request):
    raw_body = request.body.decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
