# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest24071(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
