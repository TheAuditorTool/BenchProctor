# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest61763(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
