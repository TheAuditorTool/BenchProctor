# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest06799(request):
    xml_value = request.body.decode('utf-8')
    data = coalesce_blank(xml_value)
    int(str(data))
    return JsonResponse({"saved": True})
