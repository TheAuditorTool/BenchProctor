# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25193(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value}'
    int(str(data))
    return JsonResponse({"saved": True})
