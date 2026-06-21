# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest44048(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
