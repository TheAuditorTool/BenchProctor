# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30179(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
