# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import unquote


def BenchmarkTest57294(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
