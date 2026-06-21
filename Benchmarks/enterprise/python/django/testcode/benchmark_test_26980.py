# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest26980(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    requests.get(str(data))
    return JsonResponse({"saved": True})
