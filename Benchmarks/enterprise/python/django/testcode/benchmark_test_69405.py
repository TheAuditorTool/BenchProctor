# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest69405(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    eval(str(graphql_var))
    return JsonResponse({"saved": True})
