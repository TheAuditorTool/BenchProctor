# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest16140(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
