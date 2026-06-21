# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest71452(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    requests.get(str(data))
    return JsonResponse({"saved": True})
