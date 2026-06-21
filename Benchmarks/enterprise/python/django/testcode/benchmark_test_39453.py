# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest39453(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    requests.get(str(data))
    return JsonResponse({"saved": True})
