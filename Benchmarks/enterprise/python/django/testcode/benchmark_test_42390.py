# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest42390(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
