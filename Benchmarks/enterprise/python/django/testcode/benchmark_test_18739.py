# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest18739(request, path_param):
    path_value = path_param
    sys.path.insert(0, str(path_value))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
