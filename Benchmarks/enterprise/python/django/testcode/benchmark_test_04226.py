# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest04226(request, path_param):
    path_value = path_param
    requests.get('https://api.pycdn.io/data', params={'q': str(path_value)}, verify=True)
    return JsonResponse({"saved": True})
