# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def BenchmarkTest16068(request, path_param):
    path_value = path_param
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(path_value)).read()
    return JsonResponse({"saved": True})
