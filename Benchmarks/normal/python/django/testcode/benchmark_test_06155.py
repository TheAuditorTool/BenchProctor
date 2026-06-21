# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest06155(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    json.loads(data)
    return JsonResponse({"saved": True})
