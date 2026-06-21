# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43806(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
