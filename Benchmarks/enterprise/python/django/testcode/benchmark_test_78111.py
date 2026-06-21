# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest78111(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = str(json_value).replace('\x00', '')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
