# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest13566(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    requests.get(str(data))
    return JsonResponse({"saved": True})
