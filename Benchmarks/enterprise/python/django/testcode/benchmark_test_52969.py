# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52969(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
