# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest01063(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = ' '.join(str(json_value).split())
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
