# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50157(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
