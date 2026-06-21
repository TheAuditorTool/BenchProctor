# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest20064(request, path_param):
    path_value = path_param
    requests.get(str(path_value))
    return JsonResponse({"saved": True})
