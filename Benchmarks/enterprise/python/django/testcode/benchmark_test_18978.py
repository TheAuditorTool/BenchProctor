# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest18978(request, path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    requests.get(str(data))
    return JsonResponse({"saved": True})
