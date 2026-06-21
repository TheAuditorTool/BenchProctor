# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest51050(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
