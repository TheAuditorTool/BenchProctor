# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest10072(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
