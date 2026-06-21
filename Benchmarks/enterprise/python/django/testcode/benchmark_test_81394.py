# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest81394(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    requests.get(str(data))
    return JsonResponse({"saved": True})
