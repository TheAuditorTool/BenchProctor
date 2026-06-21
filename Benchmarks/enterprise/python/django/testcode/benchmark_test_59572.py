# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59572(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    eval(str(data))
    return JsonResponse({"saved": True})
