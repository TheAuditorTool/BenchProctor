# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest75068(request):
    xml_value = request.body.decode('utf-8')
    requests.get('https://api.pycdn.io/data', params={'q': str(xml_value)}, verify=False)
    return JsonResponse({"saved": True})
