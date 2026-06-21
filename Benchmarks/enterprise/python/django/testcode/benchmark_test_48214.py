# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48214(request):
    xml_value = request.body.decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
