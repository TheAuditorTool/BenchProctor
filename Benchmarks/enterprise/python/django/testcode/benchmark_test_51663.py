# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest51663(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
