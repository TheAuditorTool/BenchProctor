# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import urllib.request


def BenchmarkTest15536(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
