# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def relay_value(value):
    return value

def BenchmarkTest02428(request):
    xml_value = request.body.decode('utf-8')
    data = relay_value(xml_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
