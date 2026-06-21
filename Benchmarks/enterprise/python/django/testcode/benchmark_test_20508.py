# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest20508(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
