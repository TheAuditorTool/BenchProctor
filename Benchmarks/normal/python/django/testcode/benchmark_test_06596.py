# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06596(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
