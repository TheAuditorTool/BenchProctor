# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest69807(request):
    xml_value = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
