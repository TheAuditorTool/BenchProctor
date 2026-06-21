# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def to_text(value):
    return str(value).strip()

def BenchmarkTest03014(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
