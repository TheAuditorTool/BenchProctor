# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest57077(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
