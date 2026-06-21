# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest09297(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    requests.get(str(data))
    return JsonResponse({"saved": True})
