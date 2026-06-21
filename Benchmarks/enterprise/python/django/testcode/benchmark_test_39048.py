# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest39048(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
