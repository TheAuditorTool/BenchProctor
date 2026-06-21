# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest76496(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    requests.get(str(data))
    return JsonResponse({"saved": True})
