# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest55241(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
