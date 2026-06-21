# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest44773(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return JsonResponse({"saved": True})
