# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest61616(request):
    xml_value = request.body.decode('utf-8')
    requests.post('http://api.prod.internal/data', data=str(xml_value))
    return JsonResponse({"saved": True})
