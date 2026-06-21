# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest71376(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
