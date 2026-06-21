# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest50137(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    os.remove(str(data))
    return JsonResponse({"saved": True})
