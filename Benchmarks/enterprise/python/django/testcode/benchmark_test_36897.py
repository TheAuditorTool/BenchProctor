# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import json


def BenchmarkTest36897(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
