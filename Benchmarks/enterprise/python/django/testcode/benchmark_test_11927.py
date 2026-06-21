# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11927(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
