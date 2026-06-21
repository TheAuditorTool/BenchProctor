# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest63603(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
