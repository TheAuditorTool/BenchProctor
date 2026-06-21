# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import requests


def BenchmarkTest30476(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
