# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest18431(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
