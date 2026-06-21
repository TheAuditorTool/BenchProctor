# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest48200(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
