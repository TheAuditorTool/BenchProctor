# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest00200(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
