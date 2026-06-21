# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest46553(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    json.loads(data)
    return JsonResponse({"saved": True})
