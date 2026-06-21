# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest49708(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    prefix = ''
    data = prefix + str(json_value)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
