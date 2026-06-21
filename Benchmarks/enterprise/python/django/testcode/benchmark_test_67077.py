# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67077(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
