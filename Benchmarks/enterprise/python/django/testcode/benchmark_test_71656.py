# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest71656(request):
    xml_value = request.body.decode('utf-8')
    requests.post('https://api.prod.internal/data', data=str(xml_value), verify=True)
    return JsonResponse({"saved": True})
