# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest53852(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    requests.get(str(data))
    return JsonResponse({"saved": True})
