# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest33644(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    prefix = ''
    data = prefix + str(json_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
