# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote


def BenchmarkTest61635(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
