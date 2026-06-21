# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61506(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
