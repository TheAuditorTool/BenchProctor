# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest35395(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(graphql_var) + ',data\n')
    return JsonResponse({"saved": True})
