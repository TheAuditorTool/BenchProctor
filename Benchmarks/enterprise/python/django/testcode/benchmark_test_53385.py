# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest53385(request, path_param):
    path_value = path_param
    _resp = requests.get(str(path_value))
    exec(_resp.text)
    return JsonResponse({"saved": True})
