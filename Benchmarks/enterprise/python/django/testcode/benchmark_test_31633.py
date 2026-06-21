# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest31633(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
