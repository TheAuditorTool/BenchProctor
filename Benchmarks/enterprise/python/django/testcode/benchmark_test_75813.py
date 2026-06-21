# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest75813(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
