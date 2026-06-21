# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def relay_value(value):
    return value

def BenchmarkTest44008(request):
    xml_value = request.body.decode('utf-8')
    data = relay_value(xml_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
