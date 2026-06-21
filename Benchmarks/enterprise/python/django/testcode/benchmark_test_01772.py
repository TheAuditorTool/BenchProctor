# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from urllib.parse import unquote


def BenchmarkTest01772(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
