# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json
import requests


@dataclass
class FormData:
    payload: str

def BenchmarkTest47491(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
