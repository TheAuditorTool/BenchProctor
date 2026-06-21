# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest76954(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
