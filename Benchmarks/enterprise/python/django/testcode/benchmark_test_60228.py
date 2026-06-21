# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60228(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
