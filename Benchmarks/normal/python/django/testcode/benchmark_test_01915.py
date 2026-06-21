# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from urllib.parse import unquote


def BenchmarkTest01915(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
