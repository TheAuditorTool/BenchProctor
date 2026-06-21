# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01840(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
