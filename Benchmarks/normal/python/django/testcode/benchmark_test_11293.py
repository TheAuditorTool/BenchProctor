# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11293(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
