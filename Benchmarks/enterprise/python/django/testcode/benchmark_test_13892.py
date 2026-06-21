# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def to_text(value):
    return str(value).strip()

def BenchmarkTest13892(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
