# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest01102(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
