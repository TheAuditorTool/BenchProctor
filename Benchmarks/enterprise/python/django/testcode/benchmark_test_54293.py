# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest54293(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
