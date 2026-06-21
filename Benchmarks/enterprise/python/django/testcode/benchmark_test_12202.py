# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest12202(request, path_param):
    path_value = path_param
    globals()['counter'] = int(path_value)
    return JsonResponse({"saved": True})
