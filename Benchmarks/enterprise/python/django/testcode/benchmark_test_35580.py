# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def BenchmarkTest35580(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
