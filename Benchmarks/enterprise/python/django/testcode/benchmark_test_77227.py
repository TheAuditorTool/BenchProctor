# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def BenchmarkTest77227(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
