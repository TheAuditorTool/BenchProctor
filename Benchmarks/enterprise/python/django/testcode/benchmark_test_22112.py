# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import unquote


def BenchmarkTest22112(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    requests.get(str(data))
    return JsonResponse({"saved": True})
