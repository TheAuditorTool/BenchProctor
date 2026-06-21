# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest74497(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    requests.get(str(graphql_var))
    return JsonResponse({"saved": True})
