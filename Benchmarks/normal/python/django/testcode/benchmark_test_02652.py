# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest02652(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    json.loads(data)
    return JsonResponse({"saved": True})
