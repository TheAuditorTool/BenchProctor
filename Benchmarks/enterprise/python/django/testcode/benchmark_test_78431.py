# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest78431(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
