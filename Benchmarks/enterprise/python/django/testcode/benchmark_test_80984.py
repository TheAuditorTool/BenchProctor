# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest80984(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    if not str(graphql_var).isdigit():
        raise Exception('error: ' + str(graphql_var))
    return JsonResponse({"saved": True})
