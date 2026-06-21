# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import requests


def BenchmarkTest09545(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(graphql_var)}, verify=False)
    return JsonResponse({"saved": True})
