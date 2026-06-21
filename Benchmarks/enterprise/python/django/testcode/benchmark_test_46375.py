# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest46375(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    if not str(graphql_var).isdigit():
        raise ValueError('invalid input: ' + str(graphql_var))
    return JsonResponse({"saved": True})
