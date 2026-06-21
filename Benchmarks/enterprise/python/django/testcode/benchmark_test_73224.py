# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest73224(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
