# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def coalesce_blank(value):
    return value or ''

def BenchmarkTest10909(request):
    xml_value = request.body.decode('utf-8')
    data = coalesce_blank(xml_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
