# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest67617(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = '%s' % (graphql_var,)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
