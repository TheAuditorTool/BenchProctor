# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json


def BenchmarkTest32276(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
