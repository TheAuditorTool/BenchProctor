# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest61133(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
